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

    $('.roupa').on('click', 'button', function(){
        $('.tbRoupa tr:last').after('<tr><td>' +  $("#tipoRoupa").val() + '</td><td></td></tr>')
    });

    /* Para enviar o token no header da requisição */
    var csrftoken = getCookie('csrftoken');
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
    
    /* Altera e atualiza a quantidade do produto no estoque */
    $('.btn-estoque').click(function() {
        var btnClicado = $(this).context.id
        $('#estoqueForm').unbind().submit(function(e) {
            e.preventDefault();
            var form = $(this).closest('form')            
            $.ajax({
                url: form.attr('action'),   // "/mov_estoque/" + form.produto.id
                data: form.serialize() + "&tipo=" + btnClicado,
                //dataType: 'json',
                method: "POST",
                success: function(dados) {
                    $('#qtd-prod-' + dados.id).text(dados.qtd)
                    //alert(dados.tipo + " de " + dados.qtd + " itens de " + dados.id)
                }
            })
        });
    });


    /* Adicionando roupas e alimentos nas tabelas de doações (funciona com tabela vazia) */
    $('.js-btn-add').click(function(e){
        var fg = $(e.target).closest(".form-group")
        var fs = $(e.target).closest("fieldset")
        
        $(fg).find('table tr:last').after(
            '<tr><td>' +  $(fs).find(".js-tipo-item").val() + '</td><td>' + $(fs).find(".js-qtd-item").val() + '</td>' +
            '<td class="text-center"><button type="button" class="close js-btn-close" style="float:none;"><span>&times;</span></button></td>' + '</tr>')

        $(fs).find(".js-tipo-item").val("")
        $(fs).find(".js-qtd-item").val("")
    });

    /* Para excluir item da tabela (não tá funcionando) */
    $('.js-btn-close').click(function(e){
        var tr = $(e.target).closest("tr")
        console.log(tr)
        
    });
});

/****** Funções para capturar o CSRF Token quando usar AJAX ******/
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}