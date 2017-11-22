from rest_framework.serializers import ModelSerializer

from django.contrib.auth.models import User
from django import forms

class UserSerializer(ModelSerializer):

	class Meta:
		model = User
		fields = [
				'username',
				'first_name',
				'last_name',
				'email',
			]
		labels = {
				'username': 'Nombre de usuario',
				'first_name': 'Nombre',
				'last_name': 'Apellidos',
				'email': 'Correo',
		}
		widgets={
			'username': forms.TextInput(attrs={'class':'form-control'}),
			'first_name': forms.TextInput(attrs={'class':'form-control'}),
			'last_name': forms.TextInput(attrs={'class':'form-control'}),
			'email': forms.TextInput(attrs={'class':'form-control'}),
			
		}
		