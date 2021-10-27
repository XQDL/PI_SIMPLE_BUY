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

    let name = document.getElementById('name').value
    let email = document.getElementById('email').value
    let phone_number = document.getElementById('phone_number').value
    let cnpj = document.getElementById('cnpj').value
    let cep = document.getElementById('cep').value
    let estado = document.getElementById('estado').value
    let cidade = document.getElementById('cidade').value
    let rua = document.getElementById('rua').value
    let numero = document.getElementById('numero').value


    num = parseInt(numero)

    


    if(name == '' || cnpj == '' || email == '' 
    || cep == '' || phone_number == '' || estado == ''
    || cidade == '' || rua == '' || numero == ''){
        raise_error("PREENCHA TODOS OS CAMPOS!", bt)
    }
    else if (!num) {
        raise_error("O CAMPO NUMERO DEVE CONTER UM VALOR NUMÉRICO!", bt)
    }
    else{
        bt.disabled = false
    }
}





