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
    metar = models.CharField(max_length=80)
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