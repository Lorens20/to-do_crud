const btnLanzarModal = document.querySelector('#lanzar-modal');
const btnOcultarModal = document.querySelector('#close-modal');
const btneditModal = document.querySelector('.edit-modal');

const contModal = document.querySelector('.contenedor-modal');


const planInput = document.querySelector('#plan');
const dateInput = document.querySelector('#date');
const placeInput = document.querySelector('#place');
const nameInput = document.querySelector('#name');

btnLanzarModal.addEventListener('click', (e) => {
    e.preventDefault();
    contModal.classList.add('mostrar');
});

btnOcultarModal.addEventListener('click', (e) => {
    e.preventDefault();
    contModal.classList.remove('mostrar');
});
btneditModal.addEventListener('click', (e) => {
      e.preventDefault();
      contModal.classList.add('mostrar');
 })