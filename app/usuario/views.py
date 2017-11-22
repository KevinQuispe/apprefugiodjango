import json
from rest_framework.views import APIView
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView,ListView
from django.core.urlresolvers import reverse_lazy
from app.usuario.forms import RegistroForm
from django.core import serializers
from app.usuario.serializers import UserSerializer

class RegistroUsuario(CreateView):	
	model = User
	template_name = 'usuario/registrar.html'
	form_class = RegistroForm
	success_url = reverse_lazy('usuario:registrar')

#funcion para serializar los objetos en formato json
def listadousuarios(request):
	lista = serializers.serialize('json', User.objects.all(), fields=['first_name','username','email'])
	return HttpResponse(lista, content_type='application/json')
class UserAPI(APIView):
	serializer = UserSerializer
	template_name = 'usuario/usaurios_list.html'
	def get(self, request, format=None):
		lista = User.objects.all()
		response = self.serializer(lista, many=True)
		return HttpResponse(json.dumps(response.data), content_type='application/json')


class ListarUsuarios(ListView):
	model=User
	tamplate_name='usuario/usuarios_list.html'