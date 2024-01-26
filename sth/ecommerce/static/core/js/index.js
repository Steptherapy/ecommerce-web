document.addEventListener("DOMContentLoaded", function () {
    const links = document.querySelectorAll('[data-target="productos-marcas"]');
    const todosLosProductos = JSON.parse('{{ productos|safe }}');
  
    links.forEach(link => {
      link.addEventListener('click', function (event) {
        event.preventDefault();
        const marcaId = link.getAttribute('data-marca-id');
        mostrarProductosPorMarca(marcaId);
      });
    });
  
    function mostrarProductosPorMarca(marcaId) {
      // Ocultar todos los productos
      const todosLosProductosDivs = document.querySelectorAll('.producto');
      todosLosProductosDivs.forEach(div => {
        div.style.display = 'none';
      });
  
      // Mostrar productos de la marca seleccionada
      const productosFiltrados = todosLosProductos.filter(prod => prod.marca_id === marcaId);
      productosFiltrados.forEach(prod => {
        const productoDiv = document.getElementById(`producto-${prod.id}`);
        if (productoDiv) {
          productoDiv.style.display = 'block';
        }
      });
    }
  });
  