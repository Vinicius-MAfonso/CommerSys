document.addEventListener("DOMContentLoaded", function () {
  const itemsContainer = document.getElementById("items-container");
  const addItemBtn = document.getElementById("addItemBtn");
  const noItemsMsg = document.getElementById("no-items-msg");
  const itemTemplate = document.getElementById("item-template");
  const totalItemsDisplay = document.getElementById("total-items");
  const totalValueDisplay = document.getElementById("total-value");
  const totalValueCard = document.getElementById("valor-total-card");

  let itemIndex = 0;

  function updateSummary() {
    const items = itemsContainer.querySelectorAll(".item-card");
    totalItemsDisplay.textContent = items.length;

    if (items.length === 0) {
      noItemsMsg.style.display = "block";
    } else {
      noItemsMsg.style.display = "none";
    }

    let total = 0;
    items.forEach((card) => {
      const subtotalText = card
        .querySelector(".item-subtotal")
        .value.replace("R$", "")
        .replace(".", "")
        .replace(",", ".")
        .trim();
      total += parseFloat(subtotalText) || 0;
    });

    const formattedTotal = total.toLocaleString("pt-BR", {
      style: "currency",
      currency: "BRL",
    });
    totalValueDisplay.textContent = formattedTotal;
    totalValueCard.textContent = formattedTotal;
  }

  function calculateSubtotal(card) {
    const qty = parseFloat(card.querySelector(".item-quantidade").value) || 0;
    const price =
      parseFloat(
        card
          .querySelector(".item-preco")
          .value.replace(".", "")
          .replace(",", ".")
      ) || 0;

    const subtotal = qty * price;
    card.querySelector(".item-subtotal").value = subtotal.toLocaleString(
      "pt-BR",
      {
        style: "currency",
        currency: "BRL",
      }
    );

    updateSummary();
  }

  function addItem() {
    const content = itemTemplate.innerHTML.replace(/\[INDEX\]/g, itemIndex);
    const div = document.createElement("div");
    div.innerHTML = content;
    const newCard = div.querySelector(".item-card");

    newCard.querySelector(".item-number").textContent =
      itemsContainer.querySelectorAll(".item-card").length + 1;
    newCard.setAttribute("data-item-index", itemIndex);

    itemsContainer.appendChild(newCard);

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

  addItemBtn.addEventListener("click", addItem);
});
