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



// ----CMO NAV onclick -----//

// function productBtn() {
//     const proNav = document.getElementById('pro-nav')
//     const updateNav = document.getElementById('update-nav')
//     const adminNav = document.getElementById('admin-nav')
//     const prperNav = document.getElementById('prper-nav')
//     const productTable = document.getElementById('product-table')
//     const updateTAble = document.getElementById('update-table')
//     const adminPoints = document.getElementById('admin-points')
//     const prdashBoard = document.getElementById('prdashboard')


//     productTable.style.display = 'block'
//     updateTAble.style.display = 'none'
//     adminPoints.style.display = 'none'
//     prdashBoard.style.display = 'none'
//     proNav.classList.add('active-inv')
//     updateNav.classList.remove('active-inv')
//     adminNav.classList.remove('active-inv')
//     prperNav.classList.remove('active-inv')
// }
// function updateBtn() {
//     const proNav = document.getElementById('pro-nav')
//     const updateNav = document.getElementById('update-nav')
//     const adminNav = document.getElementById('admin-nav')
//     const prperNav = document.getElementById('prper-nav')
//     const productTable = document.getElementById('product-table')
//     const updateTAble = document.getElementById('update-table')
//     const adminPoints = document.getElementById('admin-points')
//     const prdashBoard = document.getElementById('prdashboard')

//     productTable.style.display = 'none'
//     updateTAble.style.display = 'block'
//     adminPoints.style.display = 'none'
//     prdashBoard.style.display = 'none'
//     proNav.classList.remove('active-inv')
//     updateNav.classList.add('active-inv')
//     adminNav.classList.remove('active-inv')
//     prperNav.classList.remove('active-inv')
// }
// function adminBtn() {
//     const proNav = document.getElementById('pro-nav')
//     const updateNav = document.getElementById('update-nav')
//     const adminNav = document.getElementById('admin-nav')
//     const prperNav = document.getElementById('prper-nav')
//     const productTable = document.getElementById('product-table')
//     const updateTAble = document.getElementById('update-table')
//     const adminPoints = document.getElementById('admin-points')
//     const prdashBoard = document.getElementById('prdashboard')

//     productTable.style.display = 'none'
//     updateTAble.style.display = 'none'
//     adminPoints.style.display = 'block'
//     prdashBoard.style.display = 'none'
//     proNav.classList.remove('active-inv')
//     updateNav.classList.remove('active-inv')
//     adminNav.classList.add('active-inv')
//     prperNav.classList.remove('active-inv')
// }
// function prperBtn() {
//     const proNav = document.getElementById('pro-nav')
//     const updateNav = document.getElementById('update-nav')
//     const adminNav = document.getElementById('admin-nav')
//     const prperNav = document.getElementById('prper-nav')
//     const productTable = document.getElementById('product-table')
//     const updateTAble = document.getElementById('update-table')
//     const adminPoints = document.getElementById('admin-points')
//     const prdashBoard = document.getElementById('prdashboard')

//     productTable.style.display = 'none'
//     updateTAble.style.display = 'none'
//     adminPoints.style.display = 'none'
//     prdashBoard.style.display = 'block'
//     proNav.classList.remove('active-inv')
//     updateNav.classList.remove('active-inv')
//     adminNav.classList.remove('active-inv')
//     prperNav.classList.add('active-inv')
// }



// ----CMO NAV onclick -----//


function productBtn() {
    const productTable = document.getElementById('product-table')
    // const updateTable = document.getElementById('update-table')
    const adminPoints = document.getElementById('admin-points')
    const prdashBoard = document.getElementById('prdashboard')
    const proNav = document.getElementById('pro-nav')
    // const updateNav = document.getElementById('update-nav')
    const adminNav = document.getElementById('admin-nav')
    const prperNav = document.getElementById('prper-nav')


    productTable.style.display = 'block'
    // updateTable.style.display = 'none'
    adminPoints.style.display = 'none'
    prdashBoard.style.display = 'none'
    proNav.classList.add('active-inv')
    // updateNav.classList.remove('active-inv')
    adminNav.classList.remove('active-inv')
    prperNav.classList.remove('active-inv')
}
// function updateBtn() {

//     const productTable = document.getElementById('product-table')
//     const updateTable = document.getElementById('update-table')
//     const adminPoints = document.getElementById('admin-points')
//     const prdashBoard = document.getElementById('prdashboard')
//     const proNav = document.getElementById('pro-nav')
//     const updateNav = document.getElementById('update-nav')
//     const adminNav = document.getElementById('admin-nav')
//     const prperNav = document.getElementById('prper-nav')

//     productTable.style.display = 'none'
//     updateTable.style.display = 'block'
//     adminPoints.style.display = 'none'
//     prdashBoard.style.display = 'none'
//     proNav.classList.remove('active-inv')
//     updateNav.classList.add('active-inv')
//     adminNav.classList.remove('active-inv')
//     prperNav.classList.remove('active-inv')
// }
function adminBtn() {
    const productTable = document.getElementById('product-table')
    // const updateTable = document.getElementById('update-table')
    const adminPoints = document.getElementById('admin-points')
    const prdashBoard = document.getElementById('prdashboard')
    const proNav = document.getElementById('pro-nav')
    // const updateNav = document.getElementById('update-nav')
    const adminNav = document.getElementById('admin-nav')
    const prperNav = document.getElementById('prper-nav')


    productTable.style.display = 'none'
    // updateTable.style.display = 'none'
    adminPoints.style.display = 'block'
    prdashBoard.style.display = 'none'
    proNav.classList.remove('active-inv')
    // updateNav.classList.remove('active-inv')
    adminNav.classList.add('active-inv')
    prperNav.classList.remove('active-inv')
}
function prpercBtn() {
    const productTable = document.getElementById('product-table')
    // const updateTable = document.getElementById('update-table')
    const adminPoints = document.getElementById('admin-points')
    const prdashBoard = document.getElementById('prdashboard')
    const proNav = document.getElementById('pro-nav')
    // const updateNav = document.getElementById('update-nav')
    const adminNav = document.getElementById('admin-nav')
    const prperNav = document.getElementById('prper-nav')


    productTable.style.display = 'none'
    // updateTable.style.display = 'none'
    adminPoints.style.display = 'none'
    prdashBoard.style.display = 'block'
    proNav.classList.remove('active-inv')
    // updateNav.classList.remove('active-inv')
    adminNav.classList.remove('active-inv')
    prperNav.classList.add('active-inv')
}



const selectNav = document.getElementById('select-nav')
const staffName = document.getElementById('staff-name')
const depBtn = document.getElementById('dep-Btn')
const staffDetailsWorkdone = document.getElementById('staff-details-workdone')
const workdoneView = document.getElementById('workdone-view')


function selectBtn() {
    depBtn.style.display = 'block'
    staffDetailsWorkdone.style.display = 'none'
    workdoneView.style.display = 'none'
    staffName.display.style = 'block'
    selectNav.classList.add('activ-inv')
}
function choosestaff() {
    depBtn.style.display = 'none'
    staffDetailsWorkdone.style.display = 'none'
    workdoneView.style.display = 'none'
    staffName.display.style = 'block'
    selectNav.classList.add('activ-inv')
}


if(id2.checked==true){
    tableid.style.display='block'
}