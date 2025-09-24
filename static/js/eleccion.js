window.addEventListener('DOMContentLoaded', () => {
    const overlay = document.createElement('div');
    overlay.id = 'popupOverlay';

    overlay.innerHTML = `
    <div id="popupBox">
      <p>¿Deseas activar el modo con voz de guia?</p>
      <p>(esta acción esta diseñada para personas con perdida de visión)</p>
      <button id="btnSi">Sí</button>
      <button id="btnNo">No</button>
    </div>
  `;

    document.body.appendChild(overlay);

    document.getElementById('btnSi').addEventListener('click', () => {
        const script = document.createElement('script');
        script.src = 'sonido.js';
        document.body.appendChild(script);
        overlay.remove();
    });

    document.getElementById('btnNo').addEventListener('click', () => {
        window.location.href = 'normal';
    });

});
