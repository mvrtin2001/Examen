
$.validator.addMethod("terminaPor", function(value, element, parametro){

    if(value.endsWith(parametro)){
        return true;
    }
        return false;
}, "Debe terminar por {0}")

$("#formulario_contacto").validate({
    rules: {
        dueño: {
            required: true,
            minlength: 3,
            maxlength: 30
        },

        mascota: {
            required: true,
            minlength: 3,
            maxlength: 30
        },

        email: {
            required: true,
            email: true,
            terminaPor: "@gmail.com"
        },

        tipo_servicio: {
            required: true
        },

        mensaje: {
            required: true,
            minlength: 5,
            maxlength: 200
        }
    }
})

$("#guardar").click(function(){
    if($("#formulario_contacto").valid() == false){
        return;
    }
    let dueño = $("#dueño").val()
    let mascota = $("#mascota").val()
    let email = $("#email").val()
    let tipo_servicio = $("#tipo_servicio").val()
    let mensaje = $("#mensaje").val()
    let avisos = $("#avisos").is(":checked")
})