

document.getElementById("bt-submmit").addEventListener('click', verify)


function raise_error(err, bt){
    let err_message = document.getElementById("err-message")
    bt.disabled = true
    err_message.innerHTML = err

    setTimeout(function() { 
        bt.disabled = false
        console.log('EXEC')
    }, 1000);
}

function verify(){
    let complete_name = document.getElementById('complete_name').value
    let user_name = document.getElementById('user_name').value
    let email = document.getElementById('email').value
    let password = document.getElementById('password').value
    let phone_number = document.getElementById('phone_number').value
    let confirm_password = document.getElementById('confirm_password').value
    
    
    let bt = document.getElementById("bt-submmit")

    if(complete_name != '' & user_name != '' & email != '' 
    & password != '' & phone_number != '' & confirm_password != ''){
        bt.disabled = false
    }
    else{
        raise_error("PREENCHA TODOS OS CAMPOS!", bt)
    }

    if(password.length < 8 ){
        raise_error("A SENHA DEVE TER NO MINIMO 8 CARACTERES!!", bt)
    }
    else if(password != confirm_password){
        raise_error("AS SENHAS NÃO SÃO IGUAIS!!", bt)
    }
}




