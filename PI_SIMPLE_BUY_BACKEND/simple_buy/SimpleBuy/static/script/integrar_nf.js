document.getElementById('qtd').addEventListener('change', alterar_valor_total)
document.getElementById('ipi').addEventListener('change', alterar_valor_total)
document.getElementById('icms').addEventListener('change', alterar_valor_total)

function alterar_valor_total() {
    qtd = parseFloat(document.getElementById('qtd').value)
    vlr_un = parseFloat(document.getElementById('vlr_un').value)


    let ipi = parseFloat(document.getElementById('ipi').value)
    let icms = parseFloat(document.getElementById('icms').value)


    if(isNaN(ipi)){
        ipi = 0
    }
    if(isNaN(icms)){
        icms = 0
    }

    vlr_tot = document.getElementById('vlr_tot')

    vlr_tot.value = "R$" + ((vlr_un * qtd) * (1+(ipi/100)) * (1+(icms/100))).toFixed(2)

}