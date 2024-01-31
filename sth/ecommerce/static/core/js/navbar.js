$(document).ready(function () {
    // Desplegar menú de Marcas al pasar el ratón sobre el botón
    $("#marcasDropdownBtn").hover(
        function () {
            $(this).siblings(".dropdown-menu").toggleClass("show");
        },
        function () {
            $(this).siblings(".dropdown-menu").toggleClass("show");
        }
    );

    // Desplegar menú de Modelos al pasar el ratón sobre el botón
    $("#modelosDropdownBtn").hover(
        function () {
            $(this).siblings(".dropdown-menu").toggleClass("show");
        },
        function () {
            $(this).siblings(".dropdown-menu").toggleClass("show");
        }
    );
});

