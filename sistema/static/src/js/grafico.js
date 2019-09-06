let produtos = document.getElementById('gfProdutos').getContext('2d')
let acolhidos = document.getElementById('gfAcolhidos').getContext('2d')
let xLabel = []
let estoqueAPI = "/api/grafico/estoque";
let acolhidosAPI = "/api/grafico/acolhido";

for (let i = 1; i <= 3; i++) {
    xLabel.push(i)
}

$.ajax({
    url: estoqueAPI,
    method: "GET",
    success: function (data) {
        console.log(data)
        criaGraficoEstoque(data)
    },
    error: function() {
        
    }
})

$.ajax({
    url: acolhidosAPI,
    method: "GET",
    success: function (data) {
        console.log(data)
        criaGraficoAcolhidos(data)
    }
})

function criaGraficoEstoque(dados) {
    let graficoEstoque = new Chart(produtos, {
        type: 'bar',
        data: {
            labels: ["Quantidade disponível em estoque"],
            datasets: [{
                label: dados.nomes[0],
                backgroundColor: 'rgb(237, 192, 69, 0.5)',
                borderColor: 'rgb(237, 192, 69)',
                borderWidth: 2,
                data: [dados.qtds[0]],
                fill: false
            },
            {
                label: dados.nomes[1],
                backgroundColor: 'rgb(71, 230, 116, 0.5)',
                borderColor: 'rgb(71, 230, 116)',
                borderWidth: 2,
                data: [dados.qtds[1]],
                fill: false
            },
            {
                label: dados.nomes[2],
                backgroundColor: 'rgb(71, 196, 230, 0.5)',
                borderColor: 'rgb(71, 196, 230)',
                borderWidth: 2,
                data: [dados.qtds[2]],
                fill: false
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        stepSize: 2,
                        // suggestedMin: 5  // o mínimo vai ser esse, a não ser que tenha um valor menor
                        beginAtZero: true,  // Começa do zero
                    }
               }]
            }
        }
    })
}

function criaGraficoAcolhidos(dados) {
    let graficoAcolhidos = new Chart(acolhidos, {
        type: 'line',
        data: {
            labels: dados.anos,
            datasets: [{
                label: 'Acolhidos novos por ano',
                backgroundColor: 'rgb(237, 98, 240)',
                borderColor: 'rgb(237, 98, 240)',
                data: dados.qtds,
                fill: false
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        stepSize: 1,
                        beginAtZero: true,  // Começa do zero
                    }
                }]
            }
        }
    })
}
