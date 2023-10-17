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

// ----CMO add and calulate ------//

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
// ----CMO add and calulate ------//

function productBtn() {
    const productTable = document.getElementById('product-table')
    const updateTAble = document.getElementById('update-table')
    const proNav = document.getElementById('pro-nav')
    const updateNav = document.getElementById('update-nav')

    productTable.display.style = 'block'
    updateTAble.display.style = 'none'
    proNav.classList.add('active-product')
    updateNav.classList.remove('active-product')

}
// const calculateBtn = document.getElementById('calculateBtn')
// const addBtn = document.getElementById('addBtn')
// const calpoint = document.getElementById('cal-point')
// const addpoint = document.getElementById('add-point')

// function notipanel() {
//     const firstlineBtn = document.getElementById('firstline-Btn')
//     const targetBtn = document.getElementById('target-Btn')
//     const pendingBtn = document.getElementById('pending-Btn')
//     const notipanel = document.getElementById('notipanl-Btn')
//     const installaBtn = document.getElementById('Install-Btn')
//     const weeklyBtn = document.getElementById('weekly-Btn')

//     firstlineBtn.style.display = 'block'
//     targetBtn.style.display = 'none'
//     pendingBtn.style.display = 'none'
//     notipanel.classList.add('active-inv')
//     installaBtn.classList.remove('active-inv')
//     weeklyBtn.classList.remove('active-inv')

// }

// function installation() {
//     const firstlineBtn = document.getElementById('firstline-Btn')
//     const targetBtn = document.getElementById('target-Btn')
//     const pendingBtn = document.getElementById('pending-Btn')
//     const notipanel = document.getElementById('notipanl-Btn')
//     const installaBtn = document.getElementById('Install-Btn')
//     const weeklyBtn = document.getElementById('weekly-Btn')

//     firstlineBtn.style.display = 'none'
//     targetBtn.style.display = 'block'
//     pendingBtn.style.display = 'none'
//     notipanel.classList.remove('active-inv')
//     installaBtn.classList.add('active-inv')
//     weeklyBtn.classList.remove('active-inv')

// }
// function target() {
//     const firstlineBtn = document.getElementById('firstline-Btn')
//     const targetBtn = document.getElementById('target-Btn')
//     const pendingBtn = document.getElementById('pending-Btn')
//     const notipanel = document.getElementById('notipanl-Btn')
//     const installaBtn = document.getElementById('Install-Btn')
//     const weeklyBtn = document.getElementById('weekly-Btn')

//     firstlineBtn.style.display = 'none'
//     targetBtn.style.display = 'none'
//     pendingBtn.style.display = 'block'
//     notipanel.classList.remove('active-inv')
//     installaBtn.classList.remove('active-inv')
//     weeklyBtn.classList.add('active-inv')

// }

const firstline = document.getElementById('firstline-Btn')
const targetBtn = document.getElementById('target-Btn')
const pending = document.getElementById('pending-Btn')
const notipanlBtn = document.getElementById('notipanl-Btn')
const installBtn = document.getElementById('install-Btn')
const weeklyBtn = document.getElementById('weekly-Btn')

function notipanel() {
    firstline.style.display = 'block'
    targetBtn.style.display = 'none'
    pending.style.display = 'none'
    notipanlBtn.classList.add('active-inv')
    installBtn.classList.remove('active-inv')
    weeklyBtn.classList.remove('active-inv')
}
function installation() {
    firstline.style.display = 'none'
    targetBtn.style.display = 'block'
    pending.style.display = 'none'
    notipanlBtn.classList.remove('active-inv')
    installBtn.classList.add('active-inv')
    weeklyBtn.classList.remove('active-inv')
}
function target() {
    firstline.style.display = 'none'
    targetBtn.style.display = 'none'
    pending.style.display = 'block'
    notipanlBtn.classList.remove('active-inv')
    installBtn.classList.remove('active-inv')
    weeklyBtn.classList.add('active-inv')
}