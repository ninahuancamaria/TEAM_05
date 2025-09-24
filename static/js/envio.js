// envio.js - controla la animación del botón-camión
document.addEventListener('DOMContentLoaded', () => {
  const btn = document.getElementById('shipBtn');
  const packageEl = btn.querySelector('.package');
  const truck = btn.querySelector('.truck');
  const road = btn.querySelector('.road');
  const wheels = btn.querySelectorAll('.wheel');
  const message = btn.querySelector('.message');
  const btnText = btn.querySelector('.btn-text');

  // Duraciones/tiempos (coinciden con CSS)
  const PACKAGE_DUR = 900;     // ms
  const TRUCK_DELAY = 950;     // ms
  const TRUCK_DUR   = 2200;    // ms
  const TOTAL_TIME  = TRUCK_DELAY + TRUCK_DUR + 300; // tiempo extra para mensaje

  let animating = false;

  btn.addEventListener('click', () => {
    if (animating) return; // evita clicks múltiples durante la animación
    animating = true;

    // Reset visuales (por si)
    btn.classList.remove('animate');
    // forzar reflow para reiniciar animaciones CSS
    void btn.offsetWidth;
    // añadir clase que dispara las animaciones CSS
    btn.classList.add('animate');

    // Asegurar que elementos están en estado visible apropiado
    packageEl.style.opacity = '1';
    truck.style.opacity = '1';
    road.style.opacity = '1';
    wheels.forEach(w => w.style.opacity = '1');
    message.style.opacity = '0';

    // Desactivar el botón mientras animamos (accesibilidad)
    btn.setAttribute('disabled', 'true');

    // Después de TOTAL_TIME, limpiamos todo y dejamos listo para nuevo click
    setTimeout(() => {
      // remover clase para resetear (no antes, para que el pop del mensaje se vea)
      btn.classList.remove('animate');

      // pequeña transición de salida para elementos
      packageEl.style.opacity = '0';
      truck.style.opacity = '0';
      road.style.opacity = '0';
      wheels.forEach(w => w.style.opacity = '0');

      // Restaurar texto del botón
      message.style.opacity = '0';

      // reenabling
      btn.removeAttribute('disabled');
      animating = false;
    }, TOTAL_TIME);
  });
});
