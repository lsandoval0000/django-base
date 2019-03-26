function mensaje(mensaje, tiempo) {
    jQuery("#modal_Avisos_cuerpo").html(mensaje);
    jQuery("#modal_Avisos").modal();
    setTimeout(function () {
        jQuery('#modal_Avisos').modal('hide');
    }, tiempo);
}

function esVariable(variable) {
    return (variable !== undefined) ? true : false;
}

function errores(errores_list, campos) {
    for (index = 0; index < campos.length; index++) {
        if (esVariable(errores_list[campos[index]])) {
            $("#" + campos[index]).addClass("ui-state-error");
            $("#" + campos[index]).attr("title", errores_list[campos[index]]);
        } else {
            $("#" + campos[index]).removeClass("ui-state-error");
            $("#" + campos[index]).removeAttr("title");
        }
    }
}

function getExtension(tipo){
    var tipos = {
        "image/gif":"gif",
        "image/jpeg":"jpg",
        "image/png":"png",
        "image/tiff":"tiff",
        "image/vnd.wap.wbmp":"wbmp",
        "image/x-icon":"ico",
        "image/x-jng":"jng",
        "image/x-ms-bmp":"bmp",
        "image/svg+xml":"svg",
        "image/webp":"webp"
    };
    return tipos[tipo];
}