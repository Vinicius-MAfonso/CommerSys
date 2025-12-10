document.addEventListener("DOMContentLoaded", function () {
  const itemCanva = document.getElementById("itemCanva");
  const editButton = itemCanva.querySelector("#editButton");
  const generalActions = itemCanva.querySelector("#generalActions");
  const editActions = itemCanva.querySelector("#editActions");
  const saveButton = itemCanva.querySelector("#saveButton");
  const cancelButton = itemCanva.querySelector("#cancelButton");
  const deleteForm = document.querySelector("#deleteForm");
  const form = itemCanva.querySelector("form");
  const formFields = itemCanva.querySelectorAll("input, textarea, select");

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
    const targets = itemCanva.querySelectorAll("[data-bind]");
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
  itemCanva.addEventListener("show.bs.offcanvas", function (event) {
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
      activeRow = button.closest("tr");
      const rowData = activeRow.dataset;

      if (form && rowData.updateUrl) {
        form.action = rowData.updateUrl;
      }

      if (deleteForm && rowData.deleteUrl) {
        deleteForm.action = rowData.deleteUrl;
      }

      fillFormData(rowData);

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
        const bsOffcanvas = bootstrap.Offcanvas.getInstance(itemCanva);
        bsOffcanvas.hide();
      }
    });
  }

  itemCanva.addEventListener("hidden.bs.offcanvas", function () {
    if (form) form.reset();
    setEditMode(false);
    activeRow = null;
  });
});
