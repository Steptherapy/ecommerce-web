// Esta función se llama cuando se hace clic en el botón y desplaza la página hacia arriba
function scrollToTop() {
  window.scrollTo({
      top: 0,
      behavior: 'smooth'
  });
}

// Esta función se ejecuta cada vez que se desplaza la página
window.onscroll = function () {
  // Muestra u oculta el botón dependiendo de la posición de desplazamiento
  var btnTop = document.getElementById("btnTop");
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
      btnTop.style.display = "block";
  } else {
      btnTop.style.display = "none";
  }
};
