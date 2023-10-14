function forgot() {
    const loginform = document.getElementById('login')
    const fwd = document.getElementById('fwd')
    loginform.style.display = 'none'
    fwd.style.display = 'block'
}
function reset() {
    const loginform = document.getElementById('login')
    const fwd = document.getElementById('fwd')
    loginform.style.display = 'block'
    fwd.style.display = 'none'
}


function calInpBox() {
    const calpoint = document.getElementById('cal-point')
    const addpoint = document.getElementById('add-point')

    calpoint.style.display = 'block'
    addpoint.style.display = 'none'

}
function addInpBox() {
    const calpoint = document.getElementById('cal-point')
    const addpoint = document.getElementById('add-point')

    addpoint.style.display = 'block'
    calpoint.style.display = 'none'


}
function productBtn() {
    const calculateBtn = document.getElementById('calculate-Btn')
    const addBtn = document.getElementById('addBtn')
    const productTable = document.getElementById('product-ta')
}