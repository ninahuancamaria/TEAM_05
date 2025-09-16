const $prev = document.getElementById('prev');

$prev.addEventListener('click', () => {
  const items = document.querySelectorAll('.item');
  document.querySelector('.slide').prepend(items[items.length - 1]);
});