function navcon() {
    var navCon = document.querySelector('.nav-con')
    var rightCon = document.querySelector('.right-con')
    var rightnavlist = document.querySelectorAll('.right-nav-list')
    var smallLogo = document.querySelector('.small-logo')
    var closeIcon = document.querySelector('.close-icons')
    var menuIcon = document.querySelector('.menu-icons')
    if (navCon.style.width == '5%') {
        navCon.style.width = '18%'
        rightCon.style.width = '82%'
        for (const rightnav of rightnavlist) {
            rightnav.style.display = 'block'
        }
        smallLogo.style.display = 'none'
        closeIcon.style.display = 'block'
        menuIcon.style.display = 'none'

    }
    else {
        navCon.style.width = '5%'
        rightCon.style.width = '95%'
        for (const rightnav of rightnavlist) {
            rightnav.style.display = 'none'
        }
        smallLogo.style.display = 'block'
        closeIcon.style.display = 'none'
        menuIcon.style.display = 'block'
    }
}
function rightcon() {
    var navCon = document.querySelector('.nav-con')
    var rightCon = document.querySelector('.right-con')
    var rightnavlist = document.querySelectorAll('.right-nav-list')
    var smallLogo = document.querySelector('.small-logo')
    var closeIcon = document.querySelector('.close-icons')
    var menuIcon = document.querySelector('.menu-icons')
    navCon.style.width = '5%'
    rightCon.style.width = '95%'
    for (const rightnav of rightnavlist) {
        rightnav.style.display = 'none'
    }
    smallLogo.style.display = 'block'
    closeIcon.style.display = 'none'
    menuIcon.style.display = 'block'

}

// ===============activd nav start============

var header = document.getElementById("nav-main-con");
var btns = header.getElementsByClassName("navlistmenu");
for (var i = 0; i < btns.length; i++) {
    btns[i].addEventListener("click", function () {
        var current = document.getElementsByClassName("navlistmenu-active");
        current[0].className = current[0].className.replace(" navlistmenu-active", "");
        this.className += " navlistmenu-active";
    });
}
// ===============activd nav end============


// ===========check order button==============

const checkOrder = document.querySelectorAll('.check-order');
const orderButton = document.querySelector('#ordBtn');

checkOrder.forEach(chekBtn => {
    chekBtn.addEventListener('change', () => {
        const atLeastOneChecked = Array.from(checkOrder).some(chk => chk.checked);
        if (atLeastOneChecked) {
            orderButton.style.display = 'block';
        } else {
            orderButton.style.display = 'none';
        }
    });
});

// ===========check order button============== 


// break
var xValues = [];
var yValues = [30, 70];
var barColors = [
    "#7FA9FB",
    "#266386",
];
new Chart("myChart2", {
    type: "doughnut",
    data: {
        labels: xValues,
        datasets: [{
            backgroundColor: barColors,
            data: yValues,
            borderColor: 'transparent'
        }]
    },
    options: {
        cutoutPercentage: 80,
        title: {
            display: true,
            text: ""
        }
    }
});

//   =============leave form start========

const casualLeave = document.getElementById('casual-leaves')
const sickleave = document.getElementById('sick-leave')
const permission = document.getElementById('permission')
const casualBtn = document.getElementById('casualBtn')
const permissionBtn = document.getElementById('permissionBtn')
const sickBtn = document.getElementById('sickBtn')

casualBtn.addEventListener('click', () => {
    casualLeave.style.display = 'block'
    sickleave.style.display = 'none'
    permission.style.display = 'none'
    casualBtn.classList.add('active-forms')
    sickBtn.classList.remove('active-forms')
    permissionBtn.classList.remove('active-forms')
   
})
sickBtn.addEventListener('click', () => {
    casualLeave.style.display = 'none'
    sickleave.style.display = 'block'
    permission.style.display = 'none'
    casualBtn.classList.remove('active-forms')
    sickBtn.classList.add('active-forms')
    permissionBtn.classList.remove('active-forms')
    
})
permissionBtn.addEventListener('click', () => {
    casualLeave.style.display = 'none'
    sickleave.style.display = 'none'
    permission.style.display = 'block'
    casualBtn.classList.remove('active-forms')
    sickBtn.classList.remove('active-forms')
    permissionBtn.classList.add('active-forms')
    
})

//   =============leave form end========

const newLeaveBtn = document.getElementById('newLeave')
const leaveHistoryBtn = document.getElementById('leaveHistory')
const leaveForm = document.getElementById('leavem_con')
const leaveHistory = document.getElementById('leaveHistorys')

newLeaveBtn.addEventListener('click',()=>{
    leaveForm.style.display='block'
    leaveHistory.style.display='none'
    newLeaveBtn.classList.add('active-form-li')
    leaveHistoryBtn.classList.remove('active-form-li')
})

leaveHistoryBtn.addEventListener('click',()=>{
    leaveForm.style.display='none'
    leaveHistory.style.display='block'
    leaveHistoryBtn.classList.add('active-form-li')
    newLeaveBtn.classList.remove('active-form-li')
})

// =============late entry start===================

