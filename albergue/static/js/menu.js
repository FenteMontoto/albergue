const menu = document.querySelector('#menu')
const nav = document.querySelector('#nav')
menu.addEventListener('click', () => {
    nav.classList.toggle('active');
})


const calendario = document.querySelectorAll('.fc-past')
for (let i = 0; i < calendario.length; i++) {

    console.log(calendario[i]);

}