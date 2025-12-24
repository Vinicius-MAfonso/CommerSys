$(document).ready(function () {
  const table = $("#dataTable")
    .DataTable({
      language: {
        url: "https://cdn.datatables.net/plug-ins/1.12.1/i18n/pt-BR.json",
      },
      responsive: true,
    })
    .draw(true)
    .columns.adjust();
    $('#dataTable tbody').on('click', 'tr', function(){
        let url = $(this).data('bs-detail');
        window.location.href = url;
    })
});
