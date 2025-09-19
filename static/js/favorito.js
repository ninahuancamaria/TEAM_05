  const heartIcon = document.getElementById('heartIcon');

  heartIcon.addEventListener('click', (e) => {
    e.preventDefault(); // evita que el enlace se active
    const isFilled = heartIcon.src.includes('favorito-rojo.png');

    heartIcon.src = isFilled
      ? 'static/image/favorito.png'
      : 'static/image/favorito-rojo.png';
  });