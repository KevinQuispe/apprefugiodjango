# -*- encoding:utf-8 -*-
from django import forms
from app.adopcion.models import Persona, Solicitud
class PersonaForm(forms.ModelForm):

	class Meta:
		model = Persona
		fields = [
			'nombre',
			'apellidos',
			'edad',
			'telefono',
			'email',
			'domicilio',
		]
		labels = {
			'nombre': 'Nombre',
			'apellidos': 'Apellidos',
			'edad': 'Edad',
			'telefono': 'Teléfono',
			'email': 'Correo electrónico',
			'domicilio': 'Domicilio',
		}
		widgets = {
			'nombre':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese Nombre'}),
			'apellidos':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese Apellidos'}),
			'edad':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese Edad'}),
			'telefono':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese Telefono'}),
			'email':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese Email'}),
			'domicilio':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese domicilio'}),
		}


class SolicitudForm(forms.ModelForm):

	class Meta:
		model = Solicitud
		fields = [
			'numero_mascotas',
			'razones',	
		]
		labels = {
			'numero_mascotas': 'Numero de mascotas',
			'razones': 'Razones para adoptar',	
		}
		widgets = {
			'numero_mascotas':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese numero de mascotas'}),
			'razones':forms.Textarea(attrs={'class':'form-control','placeholder':'Ingrese las Razones por la que quiere adoptar..'}),
		}
