const menu = document.querySelector('#menu')
const nav = document.querySelector('#nav')
menu.addEventListener('click', () => {
    nav.classList.toggle('active');
})


const calendario = document.querySelector('.fc-view-container')
console.log(calendario)