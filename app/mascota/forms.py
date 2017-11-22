#importamos los form django
from django import forms
from app.mascota.models import Mascota

class MascotaForm(forms.ModelForm):

	class Meta:
		model = Mascota
		fields = [
			'nombre',
			'sexo',
			'edad_aproximada',
			'fecha_rescate',
			'persona',
			'vacuna',
		]
		labels = {
			'nombre': 'NombreMascota',
			'sexo': 'Sexo',
			'edad_aproximada': 'Edad aproximada',
			'fecha_rescate':'Fecha de rescate',
			'persona': 'Adoptante',
			'vacuna': 'Vacunas',
		}
		# los widgws son los que se van a pintar a forma de etiquetas html
		widgets={
			'nombre': forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese Nombre de mascota'}),
			'sexo': forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese sexo'}),
			'edad_aproximada': forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese edad'}),
			'fecha_rescate': forms.DateInput(attrs={'class':'form-control','placeholder':'Ingrese fecha de rescate'}),
			'persona': forms.Select(attrs={'class':'form-control'}),
			'vacuna': forms.CheckboxSelectMultiple(),
		}
		