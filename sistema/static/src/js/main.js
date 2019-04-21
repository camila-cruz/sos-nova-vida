$(document).ready(function() {
    // Adiciona uma animação para baixo quando o dropdown se expande
    $('.dropdown').on('show.bs.dropdown', function() {
        $(this).find('.dropdown-menu').first().stop(true, true).slideDown();
    });

    // Adiciona uma animação para cima quando o dropdown se retrai
    $('.dropdown').on('hide.bs.dropdown', function() {
        $(this).find('.dropdown-menu').first().stop(true, true).slideUp();
    });

    /* Formatação de inputs */
    // Máscara para CPF
    try {
        var mascaraCpf = new Cleave('.input-cpf', {
            delimiters: ['.', '.', '-'],
            blocks: [3, 3, 3, 2],
        });
    } catch (e) {}

    // Mascara para CEP
    try {
        var mascaraCep = new Cleave('.input-cep', {
            delimiters: ['-'],
            blocks: [5, 3],
        });
    } catch (e) {}

    // Máscara para telefones
    try {
        $('.input-tel').toArray().forEach(function(telefone){
            new Cleave(telefone, {
                phone: true,
                phoneRegionCode: 'BR',
            });
        });
    } catch (e) {}

    // Mascara para processos jurídicos
    try {
        var mascaraProcesso = new Cleave('.input-processo', {
            delimiters: ['-', '.', '.', '.', '.'],
            blocks: [7, 2, 4, 1, 2, 4],
        });
    } catch (e) {}

    $('#r_cep').autocompleteAddress({
        city: 'input#r_cidade',
        address: 'input#r_logradouro',
        neighborhood: 'input#r_bairro',
        state: 'input#r_uf',
    });
});

