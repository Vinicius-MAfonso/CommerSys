document.addEventListener("DOMContentLoaded", function () {
  const itemsContainer = document.getElementById("items-container");
  const addItemBtn = document.getElementById("addItemBtn");
  const noItemsMsg = document.getElementById("no-items-msg");
  const itemTemplate = document.getElementById("item-template");
  const totalItemsDisplay = document.getElementById("total-items");
  const totalValueDisplay = document.getElementById("total-value");
  const totalValueCard = document.getElementById("valor-total-card");
  const pedidoForm = document.getElementById("pedidoForm");

  let itemIndex = 0;
  let produtosCache = null;
  let isSubmitting = false;

  // Fetch products from API
  async function carregarProdutos() {
    // Show loading indicator
    const addItemBtn = document.getElementById("addItemBtn");
    const originalText = addItemBtn.innerHTML;
    addItemBtn.innerHTML = '<i class="fas fa-spinner fa-spin mr-1"></i>Carregando...';
    addItemBtn.disabled = true;

    try {
      const response = await fetch("/logistica/api/produtos/");
      if (!response.ok) {
        throw new Error(`API error: ${response.statusText}`);
      }
      const data = await response.json();
      
      if (data.success && data.produtos) {
        // Show success feedback briefly
        addItemBtn.innerHTML = '<i class="fas fa-check mr-1"></i>Pronto!';
        setTimeout(() => {
          addItemBtn.innerHTML = originalText;
          addItemBtn.disabled = false;
        }, 1000);
        
        return data.produtos;
      } else {
        console.error("Erro ao carregar produtos:", data.error || "Erro desconhecido");
        addItemBtn.innerHTML = '<i class="fas fa-exclamation-triangle mr-1"></i>Erro';
        setTimeout(() => {
          addItemBtn.innerHTML = originalText;
          addItemBtn.disabled = false;
        }, 2000);
        return [];
      }
    } catch (error) {
      console.error("Erro ao buscar produtos:", error);
      addItemBtn.innerHTML = '<i class="fas fa-exclamation-triangle mr-1"></i>Erro';
      setTimeout(() => {
        addItemBtn.innerHTML = originalText;
        addItemBtn.disabled = false;
      }, 2000);
      alert("Erro ao carregar lista de produtos. Verifique a conexão.");
      return [];
    }
  }

  // Populate product select with options
  function preencherSelectProdutos(selectElement, produtos) {
    // Clear existing options (keep only the placeholder)
    selectElement.innerHTML = '<option value="">Selecione um produto...</option>';
    
    if (!produtos || produtos.length === 0) {
      const option = document.createElement('option');
      option.disabled = true;
      option.textContent = "Nenhum produto disponível";
      selectElement.appendChild(option);
      return;
    }

    produtos.forEach((produto) => {
      const option = document.createElement("option");
      option.value = produto.id;
      option.textContent = `${produto.nome} (R$ ${parseFloat(produto.preco_base).toLocaleString("pt-BR", {minimumFractionDigits: 2, maximumFractionDigits: 2})})`;
      option.dataset.produto = JSON.stringify(produto);
      selectElement.appendChild(option);
    });
  }

  function updateSummary() {
    const items = itemsContainer.querySelectorAll(".item-card");
    totalItemsDisplay.textContent = items.length;

    if (items.length === 0) {
      noItemsMsg.style.display = "block";
    } else {
      noItemsMsg.style.display = "none";
    }

    let total = 0;
    let totalWeight = 0;
    items.forEach((card) => {
      // Parse subtotal directly since it's a currency formatted string
      const subtotalText = card.querySelector(".item-subtotal").value
        .replace("R$", "")
        .replace(/\./g, "")  // Remove thousand separators
        .replace(",", ".")   // Convert decimal comma to dot
        .trim();
      total += parseFloat(subtotalText) || 0;

      // Calculate total weight
      const qty = parseFloat(card.querySelector(".item-quantidade").value) || 0;
      const produtoSelect = card.querySelector(".item-produto");
      if (produtoSelect.value) {
        const selectedOption = produtoSelect.options[produtoSelect.selectedIndex];
        const produtoData = JSON.parse(selectedOption.dataset.produto || '{}');
        const pesoUnitario = parseFloat(produtoData.peso_unitario) || 0;
        totalWeight += qty * pesoUnitario;
      }
    });

    // Update weight fields if they exist
    const pesoBrutoInput = document.querySelector('input[name="peso_bruto"]');
    const pesoLiquidoInput = document.querySelector('input[name="peso_liquido"]');
    
    if (pesoBrutoInput && totalWeight > 0) {
      // Add 10% for packaging
      const pesoBruto = totalWeight * 1.1;
      if (window.Inputmask && $(pesoBrutoInput).inputmask) {
        $(pesoBrutoInput).inputmask('setvalue', pesoBruto);
      }
    }
    
    if (pesoLiquidoInput && totalWeight > 0) {
      if (window.Inputmask && $(pesoLiquidoInput).inputmask) {
        $(pesoLiquidoInput).inputmask('setvalue', totalWeight);
      }
    }

    const formattedTotal = total.toLocaleString("pt-BR", {
      style: "currency",
      currency: "BRL",
    });
    totalValueDisplay.textContent = formattedTotal;
    totalValueCard.textContent = formattedTotal;

    // Update freight total if freight price exists
    updateFreightTotal(total);
  }

  function updateFreightTotal(productsTotal) {
    const freightInput = document.querySelector('input[name="preco_frete"]');
    if (freightInput) {
      let freightValue = 0;
      if (window.Inputmask && $(freightInput).inputmask) {
        freightValue = parseFloat($(freightInput).inputmask('unmaskedvalue')) || 0;
      } else {
        const freightText = freightInput.value
          .replace("R$", "")
          .replace(/\./g, "")
          .replace(",", ".")
          .trim();
        freightValue = parseFloat(freightText) || 0;
      }

      const totalWithFreight = productsTotal + freightValue;
      const formattedTotalWithFreight = totalWithFreight.toLocaleString("pt-BR", {
        style: "currency",
        currency: "BRL",
      });

      // Update the total display to include freight
      const freightTotalDisplay = document.getElementById("total-with-freight");
      if (freightTotalDisplay) {
        freightTotalDisplay.textContent = formattedTotalWithFreight;
      }
    }
  }

  function calculateSubtotal(card) {
    const qty = parseFloat(card.querySelector(".item-quantidade").value) || 0;
    
    // Get the raw numeric value from the masked input
    const priceInput = card.querySelector(".item-preco");
    let priceValue = 0;
    
    if (window.Inputmask && $(priceInput).inputmask) {
      // Get unmasked value if inputmask is available
      priceValue = parseFloat($(priceInput).inputmask('unmaskedvalue')) || 0;
    } else {
      // Fallback: parse manually (Brazilian format: 123,45)
      const rawValue = priceInput.value.replace(/\./g, '').replace(',', '.');
      priceValue = parseFloat(rawValue) || 0;
    }

    const subtotal = qty * priceValue;
    
    // Format subtotal for display
    card.querySelector(".item-subtotal").value = subtotal.toLocaleString(
      "pt-BR",
      {
        style: "currency",
        currency: "BRL",
      }
    );

    updateSummary();
  }

  async function addItem() {
    // Load products if not already cached
    if (!produtosCache) {
      produtosCache = await carregarProdutos();
    }

    const content = itemTemplate.innerHTML.replace(/\[INDEX\]/g, itemIndex);
    const div = document.createElement("div");
    div.innerHTML = content;
    const newCard = div.querySelector(".item-card");

    newCard.querySelector(".item-number").textContent =
      itemsContainer.querySelectorAll(".item-card").length + 1;
    newCard.setAttribute("data-item-index", itemIndex);

    itemsContainer.appendChild(newCard);

    // Populate product select
    const selectProduto = newCard.querySelector(".item-produto");
    preencherSelectProdutos(selectProduto, produtosCache);

    // Add event listener for product selection
    selectProduto.addEventListener("change", function () {
      if (this.value) {
        const selectedOption = this.options[this.selectedIndex];
        const produtoData = JSON.parse(selectedOption.dataset.produto);
        
        // Auto-fill product details
        const precoInput = newCard.querySelector(".item-preco");
        const precoValue = parseFloat(produtoData.preco_base);
        
        // Set the raw value first, then apply mask if available
        if (window.Inputmask && $(precoInput).inputmask) {
          $(precoInput).inputmask('setvalue', precoValue);
        } else {
          // Fallback: format manually
          precoInput.value = precoValue.toLocaleString("pt-BR", { 
            minimumFractionDigits: 2, 
            maximumFractionDigits: 2 
          });
        }
        
        newCard.querySelector(".item-cfop").value = produtoData.cfop_padrao || "";
        
        // Trigger recalculation
        calculateSubtotal(newCard);
      }
    });

    // Apply input masks
    if (window.Inputmask) {
      $(newCard).find(".money-mask").inputmask("currency", {
        prefix: "",
        groupSeparator: ".",
        radicesPoint: ",",
        autoUnmask: true,
      });
      $(newCard).find(".percent-mask").inputmask("decimal", {
        radixPoint: ",",
        groupSeparator: ".",
        autoGroup: true,
        suffix: "%",
      });
    }

    newCard
      .querySelector(".item-quantidade")
      .addEventListener("input", () => calculateSubtotal(newCard));
    newCard
      .querySelector(".item-preco")
      .addEventListener("input", () => calculateSubtotal(newCard));

    newCard
      .querySelector(".remove-item-btn")
      .addEventListener("click", function () {
        newCard.remove();
        reorderItems();
        updateSummary();
      });

    itemIndex++;
    updateSummary();
  }

  function reorderItems() {
    const items = itemsContainer.querySelectorAll(".item-card");
    items.forEach((item, index) => {
      item.querySelector(".item-number").textContent = index + 1;
    });
  }

  // Initial load of products
  carregarProdutos().then((produtos) => {
    produtosCache = produtos;
    if (produtos.length === 0) {
      console.warn("Nenhum produto disponível no sistema");
    }
  });

  // Add freight price change listener
  const freightInput = document.querySelector('input[name="preco_frete"]');
  if (freightInput) {
    freightInput.addEventListener('input', function() {
      updateFreightDisplay();
      // Recalculate totals
      updateSummary();
    });
  }

  function updateFreightDisplay() {
    const freightInput = document.querySelector('input[name="preco_frete"]');
    const freightDisplay = document.getElementById("freight-display");
    
    if (freightInput && freightDisplay) {
      let freightValue = 0;
      if (window.Inputmask && $(freightInput).inputmask) {
        freightValue = parseFloat($(freightInput).inputmask('unmaskedvalue')) || 0;
      } else {
        const freightText = freightInput.value
          .replace("R$", "")
          .replace(/\./g, "")
          .replace(",", ".")
          .trim();
        freightValue = parseFloat(freightText) || 0;
      }

      freightDisplay.textContent = freightValue.toLocaleString("pt-BR", {
        style: "currency",
        currency: "BRL",
      });
    }
  }

  // Form submission handling
  if (pedidoForm) {
    pedidoForm.addEventListener('submit', function(e) {
      if (isSubmitting) {
        e.preventDefault();
        return false;
      }

      // Validate that at least one item exists
      const items = itemsContainer.querySelectorAll(".item-card");
      if (items.length === 0) {
        e.preventDefault();
        alert('Adicione pelo menos um item ao pedido.');
        return false;
      }

      // Show loading state
      isSubmitting = true;
      const submitBtn = pedidoForm.querySelector('button[type="submit"]');
      if (submitBtn) {
        const originalText = submitBtn.innerHTML;
        submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin mr-2"></i>Salvando...';
        submitBtn.disabled = true;

        // Re-enable after 10 seconds as fallback
        setTimeout(() => {
          submitBtn.innerHTML = originalText;
          submitBtn.disabled = false;
          isSubmitting = false;
        }, 10000);
      }
    });
  }

  // Keyboard shortcuts
  document.addEventListener('keydown', function(e) {
    // Ctrl + Enter to submit form
    if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
      e.preventDefault();
      const submitBtn = pedidoForm.querySelector('button[type="submit"]');
      if (submitBtn && !submitBtn.disabled) {
        submitBtn.click();
      }
    }

    // Ctrl + I to add new item
    if ((e.ctrlKey || e.metaKey) && e.key === 'i') {
      e.preventDefault();
      addItemBtn.click();
    }
  });

  addItemBtn.addEventListener("click", addItem);

  // Initialize freight display
  updateFreightDisplay();
});

