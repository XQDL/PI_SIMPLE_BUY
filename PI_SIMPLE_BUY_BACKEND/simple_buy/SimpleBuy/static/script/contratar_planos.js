let link = document.getElementById('link')

link.addEventListener('click', verify_choice)


function verify_choice(){
    let choices = document.getElementsByName('plano')
    if(choices[0].checked){
        link.href = 'registrar-administrador/1'
    }
    else if(choices[1].checked){
        link.href = 'registrar-administrador/2'
    }

    else if(choices[2].checked){
        link.href = 'registrar-administrador/3'
    }



}
