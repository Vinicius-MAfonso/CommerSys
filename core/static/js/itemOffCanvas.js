document.addEventListener("DOMContentLoaded", function () {
  const itemOffCanvas = document.getElementById("itemOffCanvas");
  const editButton = itemOffCanvas.querySelector("#editButton");
  const generalActions = itemOffCanvas.querySelector("#generalActions");
  const editActions = itemOffCanvas.querySelector("#editActions");
  const saveButton = itemOffCanvas.querySelector("#saveButton");
  const cancelButton = itemOffCanvas.querySelector("#cancelButton");
  const deleteForm = document.querySelector("#deleteForm");
  const form = itemOffCanvas.querySelector("form");
  const formFields = itemOffCanvas.querySelectorAll("input, textarea, select");

  let activeRow = null;

  function setEditMode(isEditable) {
    formFields.forEach((element) => {
      element.disabled = !isEditable;
    });
    if (saveButton) {
      saveButton.hidden = !isEditable;
      saveButton.disabled = !isEditable;
    }
    if (editActions && generalActions) {
      editActions.classList.toggle("d-none", !isEditable);
      editActions.classList.toggle("d-flex", isEditable);

      generalActions.classList.toggle("d-none", isEditable);
      generalActions.classList.toggle("d-flex", !isEditable);
    }
  }

  function fillFormData(rowData) {
    const targets = itemOffCanvas.querySelectorAll("[data-bind]");
    targets.forEach((element) => {
      const bindKey = element.getAttribute("data-bind");
      let dataValue = rowData[bindKey];

      if (dataValue !== undefined && dataValue !== "") {
        if (element.type === "number") {
          dataValue = dataValue.replace(",", ".");

          dataValue = dataValue.replace(/[^0-9.-]/g, "");

          element.value = dataValue;
        } else if (element.type === "checkbox") {
          element.checked =
            dataValue === "true" || dataValue === "True" || dataValue === "1";
        } else {
          element.value = dataValue;
        }
      } else {
        element.value = "";
      }
    });
  }
  itemOffCanvas.addEventListener("show.bs.offcanvas", function (event) {
      const button = event.relatedTarget;
      const isCreateMode = button.id === "createTrigger";

      if (isCreateMode) {
        activeRow = null;
        if (form) form.reset();
        if (form && button.dataset.createUrl) {
          form.action = button.dataset.createUrl;
        }
        setEditMode(true);
      } else {
        // Edit/View Mode
        activeRow = button.closest("tr");
        const rowData = activeRow.dataset;

        // Set form actions
        if (form && rowData.updateUrl) form.action = rowData.updateUrl;
        if (deleteForm && rowData.deleteUrl) deleteForm.action = rowData.deleteUrl;

        // Check if we have an AJAX URL for details
        if (rowData.detailUrl) {
          // 1. Visual Loading State (Optional: dim the form)
          form.style.opacity = "0.5";
          
          // 2. Fetch Data
          fetch(rowData.detailUrl)
            .then((response) => {
              if (!response.ok) throw new Error("Network response was not ok");
              return response.json();
            })
            .then((data) => {
              // 3. Fill form with fresh data from server
              fillFormData(data);
              form.style.opacity = "1";
            })
            .catch((error) => {
              console.error("Error fetching details:", error);
              form.style.opacity = "1";
              // Fallback to data attributes if fetch fails
              fillFormData(rowData);
            });
        } else {
          // Fallback: Use existing data attributes if no URL provided
          fillFormData(rowData);
        }

        setEditMode(false);
      }
    });

  if (editButton) {
    editButton.addEventListener("click", function () {
      setEditMode(true);
    });
  }

  if (cancelButton) {
    cancelButton.addEventListener("click", function () {
      if (activeRow) {
        fillFormData(activeRow.dataset);
        setEditMode(false);
      } else {
        const bsOffCanvas = bootstrap.Offcanvas.getInstance(itemOffCanvas);
        bsOffCanvas.hide();
      }
    });
  }

  itemOffCanvas.addEventListener("hidden.bs.offcanvas", function () {
    if (form) form.reset();
    setEditMode(false);
    activeRow = null;
  });
});
