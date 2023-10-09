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
        smallLogo.style.visibility = 'hidden'

    }
    else {
        navCon.style.width = '5%'
        rightCon.style.width = '95%'
        for (const rightnav of rightnavlist) {
            rightnav.style.display = 'none'
        }
        smallLogo.style.visibility = 'visible'
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
    smallLogo.style.visibility = 'visible'

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
      var yValues = [ 30,70];
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
