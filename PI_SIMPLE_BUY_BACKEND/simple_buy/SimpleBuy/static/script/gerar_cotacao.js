document.getElementById('unitario').addEventListener('change', atualize)
document.getElementById('ipi').addEventListener('change', atualize)
document.getElementById('icms').addEventListener('change', atualize)

document.getElementById("bt-submmit").addEventListener('click', verify)


function raise_error(err, bt){
    bt.disabled = true

    let err_message = document.getElementById("err-message")
    err_message.innerHTML = err

    setTimeout(function() { 
        bt.disabled = false
        console.log('EXEC')
    }, 2000);
}

function verify(){
    let bt = document.getElementById("bt-submmit")

    bt.disabled = true

    let fornecedor = document.getElementById('fornecedor').value
    let vlr_unitario = document.getElementById('unitario').value
    let ipi = document.getElementById('ipi').value
    let icms = document.getElementById('icms').value



    


    if(fornecedor == '' || vlr_unitario == '' || ipi == '' 
    || icms == '' ){
        raise_error("PREENCHA TODOS OS CAMPOS!", bt)
    }
    else{
        bt.disabled = false
    }
}

function atualize(){


    let vlr_unitario = parseFloat(document.getElementById('unitario').value)
    let ipi = parseFloat(document.getElementById('ipi').value)
    let icms = parseFloat(document.getElementById('icms').value)
    let vlr_tot_s_ipt_value = parseFloat(document.getElementById('vlr_total_s_ipt').value)
    let vlr_tot_c_ipt_value = parseFloat(document.getElementById('vlr_total_c_ipt').value)
    let quantidade = parseFloat(document.getElementById('qtd').value)

    let vlr_tot_s_ipt = document.getElementById('vlr_total_s_ipt')
    let vlr_tot_c_ipt = document.getElementById('vlr_total_c_ipt')

    vlr_tot_s_ipt.value = "R$" + quantidade * vlr_unitario


    if(isNaN(ipi)){
        ipi = 0
    }
    if(isNaN(icms)){
        icms = 0
    }


    vlr_tot_c_ipt.value = "R$" + ((vlr_unitario * quantidade) * (1+(ipi/100)) * (1+(icms/100))).toFixed(2)



}