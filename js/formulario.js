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
        event.preventDefault();
        return;
    }
    //validar que el rut contenga guión antes del último caracter
    if (rut.charAt(rut.length - 2) !== "-") {
        alert("El rut debe contener un guión");
        event.preventDefault();
        return;
    }
    //validar que el rut no se escriba con puntos
    if (rut.indexOf(".") !== -1) {
        alert("El rut no debe contener puntos");
        event.preventDefault();
        return;
    }
    //validar que el numero de telefono no supere los 9 dígitos
    if (telefono.length > 9) {
        alert("El número de telefono ingresado no sigue un formato válido")
        event.preventDefault();
        return;
    }

    alert("¡Registrado Correctamente!")    
});
