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

$('.cep').inputmask({
    mask: ['99999-999'],
    keepStatic: true,
    placeholder: "0",
    showMaskOnHover: false,
    showMaskOnFocus: false,
    clearMaskOnLostFocus: true
});

$('.cpf_cnpj').inputmask({
    mask: ['999.999.999-99', '99.999.999/9999-99'],
    keepStatic: true,
    placeholder: "0",
    showMaskOnHover: false,
    showMaskOnFocus: false,
    clearMaskOnLostFocus: true
});

$('.cnpj').inputmask({
    mask: '99.999.999/9999-99',
    placeholder: "0",
    showMaskOnHover: false,
    showMaskOnFocus: false,
    clearIncomplete: true
});

$('.ncm').inputmask({
    mask: '9999.99.99',
    placeholder: "0",   
    showMaskOnHover: false,
    showMaskOnFocus: false, 
    clearMaskOnLostFocus: true,
});

$('.ie').inputmask({
    mask: '999.999.999.999',
    placeholder: "0",   
    showMaskOnHover: false,
    showMaskOnFocus: false, 
    clearMaskOnLostFocus: true,
});


$('.phone').inputmask({
    mask: '(99) 9999-9999[9]',
    placeholder: "0",   
    showMaskOnHover: false,
    showMaskOnFocus: false, 
    clearMaskOnLostFocus: true,
});