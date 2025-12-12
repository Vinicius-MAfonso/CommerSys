document.addEventListener("DOMContentLoaded", function () {
  const itemOffcanvas = document.getElementById("itemOffcanvas");
  const editButton = itemOffcanvas.querySelector("#editButton");
  const generalActions = itemOffcanvas.querySelector("#generalActions");
  const editActions = itemOffcanvas.querySelector("#editActions");
  const saveButton = itemOffcanvas.querySelector("#saveButton");
  const cancelButton = itemOffcanvas.querySelector("#cancelButton");
  const deleteForm = document.querySelector("#deleteForm");
  const form = itemOffcanvas.querySelector("form");
  const formFields = itemOffcanvas.querySelectorAll("input, textarea, select");

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
    const targets = itemOffcanvas.querySelectorAll("[data-bind]");
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
  itemOffcanvas.addEventListener("show.bs.offcanvas", function (event) {
    const button = event.relatedTarget;

    const isCreateMode = button.id === "criarTrigger";

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
        const bsOffcanvas = bootstrap.Offcanvas.getInstance(itemOffcanvas);
        bsOffcanvas.hide();
      }
    });
  }

  itemOffcanvas.addEventListener("hidden.bs.offcanvas", function () {
    if (form) form.reset();
    setEditMode(false);
    activeRow = null;
  });
});
