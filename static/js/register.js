$(document).ready(function () {
    $("#archivoAvatar").change(function () {
        let $files = $(this).get(0).files;

        if ($files.length) {

            if ($files[0].size > $(this).data("max-size") * 1024) {
                mensaje("Please select a smaller file",2000);
                console.log("Please select a smaller file");
                return false;
            }

            console.log("Uploading file to Imgur..");

            let apiUrl = 'https://api.imgur.com/3/image';
            let apiKey = 'b00f6e54e9012d2';

            let settings = {
                async: false,
                crossDomain: true,
                processData: false,
                contentType: false,
                type: 'POST',
                url: apiUrl,
                headers: {
                    Authorization: 'Client-ID ' + apiKey,
                    Accept: 'application/json'
                },
                mimeType: 'multipart/form-data'
            };

            let formData = new FormData();
            formData.append("image", $files[0]);
            settings.data = formData;

            $.ajax(settings).done(function (response) {
                nombre = JSON.parse(response).data.id+"."+getExtension(JSON.parse(response).data.type);
                $("#avatar").val(nombre)
            });
            $(this).next('label').text($(this).val().split(/(\\|\/)/g).pop());
        }
    });

    $("#f_register").on('submit', function(e){
        e.preventDefault();
        let datos = new FormData(this);
        datos.append("avatar", $("#avatar").val());
        $.ajax({
            url: '/usuarios/register',
            data: datos,
            contentType: false,
            processData: false,
            type: 'post',
            success: function (response) {
                window.location = '/principal/panel'
            },
            statusCode: {
                404: function(responseObject, textStatus, jqXHR) {
                    mensaje("Can not find the resource!",2000);
                },
                400: function(responseObject, textStatus, jqXHR) {
                    let container, inputs, index;
                    campos = [];

                    container = document.getElementById('f_register');

                    inputs = container.getElementsByTagName('input');
                    for (index = 0; index < inputs.length; ++index) {
                        if(inputs[index].id.length > 0)
                            campos.push(inputs[index].id);
                    }
                    errores(responseObject.responseJSON.errores, campos);
                    mensaje("Check the errors",2000);
                },
                500: function(responseObject, textStatus, errorThrown) {
                    mensaje("Something went wrong!",2000);
                }          
            }
        });
    });
});