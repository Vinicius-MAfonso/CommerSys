document.addEventListener("DOMContentLoaded", function (){
    let deleteModal = document.getElementById("deleteModal");
    let deleteForm = document.getElementById("deleteForm");

    deleteModal.addEventListener("show.bs.modal", function (event) {
        let button = event.relatedTarget;
        let url = button.getAttribute("data-url");
        deleteForm.action = url;
    });
}
)