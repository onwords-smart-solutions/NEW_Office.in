// function login() {
//     const signUpButton = document.getElementById('signUp');
//     const signInButton = document.getElementById('signIn');
//     const main = document.getElementById('main');

//     signUpButton.addEventListener('click', () => {
//         main.classList.add("right-panel-active");
//     });
//     signInButton.addEventListener('click', () => {
//         main.classList.remove("right-panel-active");
//     });
// }

// const overlayContainer = document.querySelector('.overlay-container')
// const signBtn = document.getElementById('signIn')
// const signUpBtn = document.getElementById('signUp')
// const signInBtnView = document.getElementById('sign-view-btn')
// const signUpBtnView = document.getElementById('signup-view-btn')

// signUpBtn.addEventListener('click', () => {
//     overlayContainer.style.left = '0%'
//     signInBtnView.style.display = 'block'
//     signUpBtnView.style.display = 'none'
// })
// signInBtnView.addEventListener('click', () => {
//     // overlayContainer.style.right = '0%'
//     signInBtnView.style.display = 'none'
//     signUpBtnView.style.display = 'block'
// })

function login() {
    const loginBtn = document.getElementById('loginBtn')
    const signinBtn = document.getElementById('signBtn')
    const overcon = document.querySelector('.over')
    const loginWel = document.querySelector('.login-wel')
    const signWel = document.querySelector('.sign-wel')

    loginBtn.addEventListener('click', () => {
        overcon.style.left = '0%'
        loginBtn.style.display='none'
        signinBtn.style.display='block'
        loginWel.style.display='none'
        signWel.style.display='block'
        


    })

    signinBtn.addEventListener('click', () => {
        overcon.style.left = '50%'
        loginBtn.style.display='block'
        signinBtn.style.display='none'
        loginWel.style.display='block'
        signWel.style.display='none'

    })
}