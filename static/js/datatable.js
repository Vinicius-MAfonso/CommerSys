$(document).ready(function () {
  const table = $("#dataTable").DataTable({
    language: {
      url: "https://cdn.datatables.net/plug-ins/1.12.1/i18n/pt-BR.json",
    },
    responsive: true,
  });

  $('#dataTable tbody').on('click', 'tr', function () {
    const url = $(this).data('bs-detail');

    if (url && url !== undefined) {
      window.location.href = url;
    }
  });
});