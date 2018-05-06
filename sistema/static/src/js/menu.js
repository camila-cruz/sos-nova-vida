document.getElementById("menuLateral").innerHTML =
'<div>' +
    '<div class="navbar-header">' +
        '<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#collapse-navbar" aria-expanded="false">' +
            '<span class="sr-only">Toggle navigation</span>' +
            '<span class="icon-bar"></span>' +
            '<span class="icon-bar"></span>' +
            '<span class="icon-bar"></span>' +
            '<span class="icon-bar"></span>' +
        '</button>' +
        //'<a class="navmenu-brand" href="index.html"><h3>SOS Nova Vida</h3></a>' +
    '</div>' +
    '<div class="collapse navbar-collapse" id="collapse-navbar">' +
        '<ul class="nav navmenu-nav col-md-12">' +
            '<li role="presentation" class="dropdown">' +
                '<a class="dropdown-toggle" data-toggle="dropdown" href="#" role="button" aria-haspopup="true" aria-expanded="false">' +
                '<span class="glyphicon glyphicon-heart-empty"></span>&nbsp;&nbsp;&nbsp;' +
                'Acolhidos <span class="caret"></span></a>' +
                '<ul class="dropdown-menu">' +
                    '<li><a href="formAcolhido.html">Cadastrar</a></li>' +
                    '<li><a href="consultaAcolhido.html">Consultar</a></li>' +
                '</ul>' +
            '</li>' +
            
            '<li class="dropdown">' +
                '<a class="dropdown-toggle" data-toggle="dropdown" href="#">' +
                '<span class="glyphicon glyphicon-thumbs-up"></span>&nbsp;&nbsp;&nbsp;' +
                'Doadores <span class="caret"></span></a>' +
                '<ul class="dropdown-menu">' +
                    '<li><a href="formDoador.html">Cadastrar</a></li>' +
                    '<li><a href="consultaDoador.html">Consultar</a></li>' +
                '</ul>' +
            '</li>' +
            
            '<li class="dropdown">' +
                '<a class="dropdown-toggle" data-toggle="dropdown" href="#">' +
                '<span class="glyphicon glyphicon-shopping-cart"></span>&nbsp;&nbsp;&nbsp;' +
                'Estoque </a>' +
                /*'<ul class="dropdown-menu">' +
                    '<li><a href="formProduto.html">Cadastrar produto</a></li>' +
                    '<li><a href="consultaEstoque.html">Gerenciar</a></li>' +
                    //'<li><a>Retirar produto</a></li>' +
                '</ul>' +*/
            '</li>' +

            //'<li><a href="formContabilidade.html">Contabilidade</a></li>' +
            '<li class="dropdown">' +
                '<a class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">' +
                '<span class="glyphicon glyphicon-gift"></span>&nbsp;&nbsp;&nbsp;' +
                'Doações <span class="caret"></span></a>' +
                '<ul class="dropdown-menu">' +
                    '<li><a href="formDoacoes.html">Cadastrar</a></li>' +
                    '<li><a href="">Consultar</a></li>' +
                '</ul>' +
            '</li>' +
            '<li>' +
                '<a href="formConfig.html">' + 
                '<span class="glyphicon glyphicon-cog"></span>&nbsp;&nbsp;&nbsp;' +
                'Configurações</a>' +
            '</li>' +
            //'<li><a>Usuários</a></li>' +
            //'<li><a>Configurações</a></li>' +
        '</ul>' +
    '</div>' +
'</div>'
;

// Adiciona uma animação para baixo quando o drpdown se expande
$('.dropdown').on('show.bs.dropdown', function() {
    $(this).find('.dropdown-menu').first().stop(true, true).slideDown();
});

// Adiciona uma animação para cima quando o dropdown se retrai
$('.dropdown').on('hide.bs.dropdown', function() {
    $(this).find('.dropdown-menu').first().stop(true, true).slideUp();
});