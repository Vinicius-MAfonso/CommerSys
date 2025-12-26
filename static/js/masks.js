$('.moeda').inputmask('currency', {
    radixPoint: ',',
    groupSeparator: '.',
    autoGroup: true,
    allowMinus: false,
    prefix: 'R$ ',
    digits: 2,
    rightAlign: true,
    removeMaskOnSubmit: true 
});

$('.cpf_cnpj').inputmask({
    mask: ['999.999.999-99', '99.999.999/9999-99'],
    keepStatic: true
});

$('.cnpj').inputmask({
    mask: ['99.999.999/9999-99'],
    keepStatic: true
})

