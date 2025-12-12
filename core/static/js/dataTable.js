const dataTable = $("#table").DataTable({
  responsive: true,
  layout: {
    topStart: {
      buttons: [
        {
          text: '<i class="fas fa-plus"></i> Novo',
          className: 'btn btn-success', 
          action: function (e, dt, node, config) {
            document.getElementById('criarTrigger').click();
          }
        }
      ]
    }
  },
  columnDefs: [],
  info: false,
  lengthMenu: [10, 25, 50, 100],

  stateSave: true,
  language: {
    url: "https://cdn.datatables.net/plug-ins/2.1.8/i18n/pt-BR.json",
  },
});

