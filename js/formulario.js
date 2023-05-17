$(document).ready(function() {
    $("#mostrarBtn").click(function() {
        $("#formulario").show(500);
    });
});

$(document).ready(function() {
    $("#ocultarBtn").click(function() {
        $("#formulario").hide(500);
    });
});  

document.getElementById("formulario").addEventListener("submit", function(event) {
    var nombre = document.getElementById("nombre").value;
    var apellidoPaterno = document.getElementById("apellidoPaterno").value;
    var apellidoMaterno = document.getElementById("apellidoMaterno").value;
    var rut = document.getElementById("rut").value;
    var direccion = document.getElementById("direccion").value;
    var telefono = document.getElementById("telefono").value;
    var email = document.getElementById("email").value;
    var genero = document.getElementById("genero").value;

    if (nombre === "" || apellidoPaterno === "" || apellidoMaterno === "" || rut === "" || direccion === "" || telefono === "" || email === "" || genero === "") {
    alert("Por favor, completa todos los campos");
    return;
    }

    alert("¡Registrado Correctamente!")    
});
