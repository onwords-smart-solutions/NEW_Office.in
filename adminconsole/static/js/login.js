function forgot(){
    const loginform = document.getElementById('login')
    const fwd = document.getElementById('fwd')
    loginform.style.display='none'
    fwd.style.display='block'
}
function reset(){
    const loginform = document.getElementById('login')
    const fwd = document.getElementById('fwd')
    loginform.style.display='block'
    fwd.style.display='none'
}