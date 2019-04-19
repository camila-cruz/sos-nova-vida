$(document).ready(function() {
    // Adiciona bootstrap aos inputs necessários
    $('input:not(:checkbox, :radio)').addClass("form-control");
    //$('input:checkbox').removeClass("form-control");
    $('select').addClass("form-control");
    
    // Colocar um try aqui: não abre a página de estoque depois de abrir a página de configuração
    document.getElementById("id_imagem").type = "file";

    // IDs dos inputs que contém data
    var data = ["id_data_nasc", "id_data_entrada", "id_data", "id_data_validade"];
    
    // Para cada input, se não for nulo, adicionar o type 'date'
    for (i = 0; i < 4; i++) {
        if (data[i] !== null) {
            document.getElementById(data[i]).type = "date";
            console.log(i);
        }
    }

    /* Formatação de inputs */
    var mascaraCpf = new Cleave('.input-cpf', {
        delimiters: ['.', '.', '-'],
        blocks: [3, 3, 3, 2]
    });

    var mascaraTel = new Cleave ('.input-tel', {
        phone: true,
        phoneRegionCode: 'BR',
    });
});

function clean() {
    $('#txt_pia').val('');
}