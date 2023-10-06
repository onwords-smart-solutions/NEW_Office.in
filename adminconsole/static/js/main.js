function navcon() {
    var navCon = document.querySelector('.nav-con')
    var rightCon = document.querySelector('.right-con')
    var rightnavlist = document.querySelectorAll('.right-nav-list')
    var smallLogo = document.querySelector('.small-logo')
    if (navCon.style.width == '5%') {
        navCon.style.width = '18%'
        rightCon.style.width = '82%'
        for (const rightnav of rightnavlist) {
            rightnav.style.display = 'block'
        }
        smallLogo.style.visibility='hidden'

    }
    else {
        navCon.style.width = '5%'
        rightCon.style.width = '95%'
        for (const rightnav of rightnavlist) {
            rightnav.style.display = 'none'
        }
        smallLogo.style.visibility='visible'
    }
}
function rightcon() {
    var navCon = document.querySelector('.nav-con')
    var rightCon = document.querySelector('.right-con')
    var rightnavlist = document.querySelectorAll('.right-nav-list')
    var smallLogo = document.querySelector('.small-logo')
    navCon.style.width = '5%'
    rightCon.style.width = '95%'
    for (const rightnav of rightnavlist) {
        rightnav.style.display = 'none'
    }
    smallLogo.style.visibility='visible'

}


// ===============activd nav start============
var header = document.getElementById("nav-main-con");
var btns = header.getElementsByClassName("navlistmenu");
for (var i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", function() {
  var current = document.getElementsByClassName("navlistmenu-active");
  current[0].className = current[0].className.replace(" navlistmenu-active", "");
  this.className += " navlistmenu-active";
  });
}
// ===============activd nav end============