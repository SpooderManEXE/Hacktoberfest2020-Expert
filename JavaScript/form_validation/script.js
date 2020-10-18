const name = document.getElementById('name')
const password= document.getElementById('password')
const email = document.getElementById('email')
const form = document.getElementById('form')
const errorElement = document.getElementById('error')

form.addEventListener('submit', (e) =>{
    let messages = []
    if (name.value === '' || name.value == null){
        messages.push('name is required')
    }

    if (password.value.length <= 8){
        messages.push('password must be longer than 8')
    }

    if(password.value === 'password'){
        messages.push('password cannot be password')
    }

    

    if (messages.length > 0 ){
        e.preventDefault()
        errorElement.innerText = messages.join(', ')
    }
})