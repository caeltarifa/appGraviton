function validatornumero2(object){
    if  (object.value.length > object.maxLength){
        object.value = object.value.slice(0, object.maxLength)
    }
}



function validarform(){
    tipomsj = document.getElementById('idtipomsj').value;
    lugar=document.getElementById('idlugar').value;

    dia=document.getElementById('iddia').value;
    if (dia.length==1) {
        dia = '0'+dia;
    }
    hora=document.getElementById('idhora').value;
    if (hora.length==1) {
        hora = '0'+hora;
    }

    minuto=document.getElementById('idminuto').value;
    if (minuto.length==1) {
        minuto = '0'+minuto;
    }
    
    direcviento=document.getElementById('iddireccionviento').value;
    intensidad=document.getElementById('idintensidad').value;
    tipoviento1=document.getElementById('idtipoviento1').value;
    tipoviento2=document.getElementById('idtipoviento2');
    
    // if (document.getElementById('idtipoviento2').checked) {
    //     //alert(tipoviento2)
    // }
    rafaga=document.getElementById('idrafaga').value;
    direcv1=document.getElementById('iddireccion1').value;
    direcv2=document.getElementById('iddireccion2').value;

    visibilidad1=document.getElementById('idvisibilidad1').value;
    direcvisib1=document.getElementById('iddireccionvisibilidad1').value;
    visibilidad2=document.getElementById('idvisibilidad2').value;
    direcvisib2=document.getElementById('iddireccionvisibilidad2').value;

    fenomeno1=document.getElementById('idfenomeno1').value;
    fenomeno2=document.getElementById('idfenomeno2').value;
    fenomeno3=document.getElementById('idfenomeno3').value;

    nubosidad1=document.getElementById('idnubosidad1').value;
    nubosidadvalor1=document.getElementById('idnubosidadvalor1').value;
    nubosidad2=document.getElementById('idnubosidad2').value;
    nubosidadvalor2=document.getElementById('idnubosidadvalor2').value;
    nubosidad3=document.getElementById('idnubosidad3').value;
    nubosidadvalor3=document.getElementById('idnubosidadvalor3').value;

    temperatura=document.getElementById('idtemperatura').value;
    temperaturarocio=document.getElementById('idtemperaturarocio').value;
    humedadrelativa=document.getElementById('idhumrelativa').value;
    qnh=document.getElementById('idqnh').value;

    pasocord1=document.getElementById('idpasocordi1').value;
    pasocord2=document.getElementById('idpasocordi2').value;
    pasocord3=document.getElementById('idpasocordi3').value;
    pasocord4=document.getElementById('idpasocordi4').value;

    nota=document.getElementById('idnota').value;
    tipofin=document.getElementById('idtipofin').value;
    fin=document.getElementById('idfin').value;

        $('#idresultado').val( ( 'METAR '+  lugar + (' ' +dia+hora+'Z ') ) +
                                        (direcviento + ' ' +intensidad + (tipoviento2.checked? ('G'+rafaga): 'KT') + ( ' '+direcv1+'V'+direcv2)) + 
                                        (' ' + visibilidad1+direcvisib1 + ' ' +visibilidad2+direcvisib2)+
                                        (fenomeno1+' '+fenomeno2+ ' ' +fenomeno3)+
                                        (nubosidad1+nubosidadvalor1 +' ' + nubosidad2+nubosidadvalor2+' '+nubosidad3+nubosidadvalor3)+
                                        (' '+temperatura+'/'+temperaturarocio + ' '+ humedadrelativa+ ' ' +qnh + (lugar=='SLLP'? 'P'+pasocord1+pasocord2+pasocord3+pasocord4: '' ))+
                                        (nota + ' ' +tipofin + fin)
                                        )


}



function validarform2(){
    tipomsj = document.getElementById('idtipomsj').value;
    lugar=document.getElementById('idlugar').value;

    dia=document.getElementById('iddia').value;
    if (dia.length==1) {
        dia = '0'+dia;
    }
    hora=document.getElementById('idhora').value;
    if (hora.length==1) {
        hora = '0'+hora;
    }

    minuto=document.getElementById('idminuto').value;
    if (minuto.length==1) {
        minuto = '0'+minuto;
    }
    
    direcviento=document.getElementById('iddireccionviento').value;
    intensidad=document.getElementById('idintensidad').value;
    tipoviento1=document.getElementById('idtipoviento1').value;
    tipoviento2=document.getElementById('idtipoviento2');
    
    // if (document.getElementById('idtipoviento2').checked) {
    //     //alert(tipoviento2)
    // }
    rafaga=document.getElementById('idrafaga').value;
    direcv1=document.getElementById('iddireccion1').value;
    direcv2=document.getElementById('iddireccion2').value;

    visibilidad1=document.getElementById('idvisibilidad1').value;
    direcvisib1=document.getElementById('iddireccionvisibilidad1').value;
    visibilidad2=document.getElementById('idvisibilidad2').value;
    direcvisib2=document.getElementById('iddireccionvisibilidad2').value;

    fenomeno1=document.getElementById('idfenomeno1').value;
    fenomeno2=document.getElementById('idfenomeno2').value;
    fenomeno3=document.getElementById('idfenomeno3').value;

    nubosidad1=document.getElementById('idnubosidad1').value;
    nubosidadvalor1=document.getElementById('idnubosidadvalor1').value;
    nubosidad2=document.getElementById('idnubosidad2').value;
    nubosidadvalor2=document.getElementById('idnubosidadvalor2').value;
    nubosidad3=document.getElementById('idnubosidad3').value;
    nubosidadvalor3=document.getElementById('idnubosidadvalor3').value;

    temperatura=document.getElementById('idtemperatura').value;
    temperaturarocio=document.getElementById('idtemperaturarocio').value;
    humedadrelativa=document.getElementById('idhumrelativa').value;
    qnh=document.getElementById('idqnh').value;

    pasocord1=document.getElementById('idpasocordi1').value;
    pasocord2=document.getElementById('idpasocordi2').value;
    pasocord3=document.getElementById('idpasocordi3').value;
    pasocord4=document.getElementById('idpasocordi4').value;

    nota=document.getElementById('idnota').value;
    tipofin=document.getElementById('idtipofin').value;
    fin=document.getElementById('idfin').value;


        $('#idresultado2').val(('SPECI '+ (lugar + (' ' +dia+hora+minuto+'Z ')) ) +
                                        (direcviento + ' ' +intensidad + (tipoviento2.checked? ('G'+rafaga): 'KT') + ( ' '+direcv1+'V'+direcv2)) + 
                                        (' ' + visibilidad1+direcvisib1 + ' ' +visibilidad2+direcvisib2)+
                                        (fenomeno1+' '+fenomeno2+ ' ' +fenomeno3)+
                                        (nubosidad1+nubosidadvalor1 +' ' + nubosidad2+nubosidadvalor2+' '+nubosidad3+nubosidadvalor3)+
                                        (' '+temperatura+'/'+temperaturarocio + ' '+ humedadrelativa+ ' ' +qnh + (lugar=='SLLP'? 'P'+pasocord1+pasocord2+pasocord3+pasocord4: '' ))+
                                        (nota + ' ' +tipofin + fin)
                                        )

}