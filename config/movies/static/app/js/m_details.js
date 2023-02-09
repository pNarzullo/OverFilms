document.getElementById('review_forms').style.display = 'none';

function review_forms() {
  document.getElementById('review_forms').style.display = 'block';
}

const button = document.querySelector('button');
const form = document.querySelector('#review_forms');

button.addEventListener('click', () => {
  form.classList.add('open');
});

