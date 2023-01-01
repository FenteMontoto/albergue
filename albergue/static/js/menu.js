const menu = document.querySelector('#menu')
const nav = document.querySelector('#nav')
menu.addEventListener('click', () => {
    nav.classList.toggle('active');
})


var links = document.getElementsByClassName('fc-event-container')

console.log(links)