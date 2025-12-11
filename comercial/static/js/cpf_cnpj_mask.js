$(document).ready(function () {
  $("#cpf_cnpj").mask("000.000.000-00", {
    onKeyPress: function (cpfcnpj, e, field, options) {
      const masks = ["000.000.000-000", "00.000.000/0000-00"];
      const mask = cpfcnpj.length > 14 ? masks[1] : masks[0];
      $("#cpf_cnpj").mask(mask, options);
    },
  });
});
