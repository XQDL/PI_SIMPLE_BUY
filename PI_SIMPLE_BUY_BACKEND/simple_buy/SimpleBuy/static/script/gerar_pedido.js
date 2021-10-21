document.getElementById('qtd').addEventListener('change', alterar_valor_unitario)

function alterar_valor_unitario(){
    qtd = parseInt(document.getElementById('qtd').value)
    vlr_un = parseFloat(document.getElementById('vlr_un').value)


    vlr_estimado = document.getElementById('vlr_estimado')

    vlr_estimado.value = 'R$' + (vlr_un * qtd)

}