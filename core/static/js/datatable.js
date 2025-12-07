const dataTable = $("#table").DataTable({
  columnDefs: [
      { targets: 'no-sort', orderable: false }
  ],
  info: false,
  lengthMenu: [10, 25, 50, 100],

  stateSave: true,
  language: {
    url: "https://cdn.datatables.net/plug-ins/2.1.8/i18n/pt-BR.json",
  },
});

