from django import forms

from apps.datagen.models import TAF_table

#FORMULARIO TAF
class Taf_generar_form(forms.ModelForm):
    
    class meta:
        model = TAF_table

        fields = [
            'dasdataf',
            'codigo_oaci',
            'pediodo_validez',
            'viento',
            'vsibilidad',
            'precipitacion',
            'capa_nublada',
            'tempo',
            'nieve',
            'cambio_viento',
            'proximo_pronostico',
        ]

        labels = {
            'ddsataf':'xxtaf',
            'codigo_oaci':'xxcodigo_oaci',
            'pediodo_validez':'xxpediodo_validez',
            'viento':'xxviento',
            'vsibilidad':'xxvsibilidad',
            'precipitacion':'xxprecipitacion',
            'capa_nublada':'xxcapa_nublada',
            'tempo':'xxtempo',
            'nieve':'xxnieve',
            'cambio_viento':'xxcambio_viento',
            'proximo_pronostico':'xxproximo_pronostico',
        }

        widgets = {
            'xxtaf':forms.TextInput(attrs={'class': 'form-control'}),
            'xxcodigo_oaci':forms.TextInput(attrs={'class': 'form-control'}),
            'xxpediodo_validez':forms.TextInput(attrs={'class': 'form-control'}),
            'xxviento':forms.TextInput(attrs={'class': 'form-control'}),
            'xxvsibilidad':forms.TextInput(attrs={'class': 'form-control'}),
            'xxprecipitacion':forms.TextInput(attrs={'class': 'form-control'}),
            'xxcapa_nublada':forms.TextInput(attrs={'class': 'form-control'}),
            'xxtempo':forms.TextInput(attrs={'class': 'form-control'}),
            'xxnieve':forms.TextInput(attrs={'class': 'form-control'}),
            'xxcambio_viento':forms.TextInput(attrs={'class': 'form-control'}),
            'xxproximo_pronostico':forms.TextInput(attrs={'class': 'form-control'}),
        }

class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {
                'class': 'form-control',
                'placeholder': field,
                'type': 'checkbox',
            }

    class Meta:
        model= TAF_table
        fields = (
            'taf',
            'codigo_oaci',
            'pediodo_validez',
            'viento',
            'vsibilidad',
            'precipitacion',
            'capa_nublada',
            'tempo',
            'nieve',
            'cambio_viento',
            'proximo_pronostico',
        )

#FORMULARIO METAR



#FORMULARIO SPECI