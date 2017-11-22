from django.conf.urls import url,include
from app.usuario.views import RegistroUsuario,ListarUsuarios,listadousuarios,UserAPI
from django.contrib.auth.decorators import login_required

urlpatterns = [
   url(r'^registrar',login_required(RegistroUsuario.as_view()), name='registrar'), 
   url(r'^api', UserAPI.as_view(), name="api"),
   url(r'^listado', listadousuarios, name="listado"),

]