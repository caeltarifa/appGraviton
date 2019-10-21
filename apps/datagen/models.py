from django.db import models

# Create your models here.
class TAF_table(models.Model):
    taf = models.CharField(max_length=80)
    codigo_oaci = models.CharField(max_length=80)
    pediodo_validez = models.CharField(max_length=80)
    viento = models.CharField(max_length=80)
    vsibilidad = models.CharField(max_length=80)
    precipitacion = models.CharField(max_length=80)
    capa_nublada = models.CharField(max_length=80)
    tempo = models.CharField(max_length=80)
    nieve = models.CharField(max_length=80)
    cambio_viento = models.CharField(max_length=80)
    proximo_pronostico = models.CharField(max_length=80)

# Create your models here.
class METAR_table(models.Model):
    metar = models.CharField(max_length=5)
    codigo_oaci = models.CharField(max_length=4)
    
    # DIA+HORA:  18 + 08Z = 1808Z
    dia_obser = models.SmallIntegerField(null=False )#max_length=2 
    hora_observ = models.SmallIntegerField(null=False )#max_length=2 
    
    viento_direc = models.SmallIntegerField(null=False ) #max_length=3 viento direccion 0 a 360grados
    viento_intens = models.SmallIntegerField(null=False ) #max_length=2 viento intensidad  
    rafaga = models.SmallIntegerField(null=False ) # max_length=2  rafaga 1-99
    viento_variable_1 = models.CharField(null=False, max_length=7 ) # max_length=3  variabilidad de viento 0 - 360
    #viento_variable_2 = models.SmallIntegerField(null=False ) # max_length=3  variabilidad de viento 0 - 360

    visibilidad_horiz_1 = models.SmallIntegerField(null=False ) #max_length=4  visibilidad horizontal 50-800 "+50" | 800-5000 "+100" | 5000-9000 "+1000" | y >9000 => 9999 CON JAVASCRIPT
    direccion_predomin = models.CharField(max_length=2) #8 opciones N NE E SE S SW W NW

    visibilidad_horiz_2 = models.SmallIntegerField(null=False ) #max_length=4 visibilidad_horiz_1<5000 => habilitar visibilidad_horiz_2  ||  visibilidad horizontal 50-800 "+50" | 800-5000 "+100" | 5000-9000 "+1000" | y >9000 => 9999
    direccion_predomin = models.CharField(max_length=2) #8 opciones N NE E SE S SW W NW

    # -- alcance_visual = models.CharField(max_length=80) #alcance visual de pista RVR
    
    tiempo_presente_1 = models.CharField(max_length=6) #fenomenos actuales lista con opciones PENDIENTE LISTA DE FENOM
    tiempo_presente_2 = models.CharField(max_length=6) #fenomenos actuales lista con opciones PENDIENTE LISTA DE FENOM
    tiempo_presente_3 = models.CharField(max_length=6) #fenomenos actuales lista con opciones PENDIENTE LISTA DE FENOM

    capa_nube = models.CharField(max_length=80) #nubosidad: PENDIENTE 4campos

    temperatura = models.SmallIntegerField(null=False ) # max_length=2       temperatura ambiente: -50 to 50
    temperatura_rocio = models.SmallIntegerField(null=False ) # max_length=80        (temperatura_rocio < temperatura )  

    qnh = models.CharField(max_length=80) #presion reducida a nivel medio del mar en condiciones de atmosfera: PENDIENTE

    humedad_relat = models.SmallIntegerField(null=False ) # max_length=3 humedad relativa (agregar %) 01-99

    pasos_cordillera = models.CharField(max_length=5) #P_,_,_,_  P5684
    
    comentario = models.CharField(max_length=80) 

    estado_pista = models.CharField(max_length=20)

# Create your models here.
class ESPECI_table(models.Model):
    speci = models.CharField(max_length=80)
    codigo_oaci = models.CharField(max_length=80)
    dia_obser = models.CharField(max_length=80)
    hora_observ = models.CharField(max_length=80)
    obser_autom = models.CharField(max_length=80)
    medida_viento = models.CharField(max_length=80)
    visibilidad_horiz = models.CharField(max_length=80)
    alcance_visual = models.CharField(max_length=80)
    tiempo_presente = models.CharField(max_length=80)
    capa_nube = models.CharField(max_length=80)
    nubes_opcion = models.CharField(max_length=80)
    temperatura = models.CharField(max_length=80)
    temperatura_rocio = models.CharField(max_length=80)
    qnh = models.CharField(max_length=80)
    estado_pista = models.CharField(max_length=80)
    comentario = models.CharField(max_length=80)
    nubes_opcion = models.CharField(max_length=80)
    presion = models.CharField(max_length=80)