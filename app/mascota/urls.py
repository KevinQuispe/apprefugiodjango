from django.conf.urls import url,include

from app.mascota.views import index, mascota_crear, mascota_list, mascota_edit, mascota_delete, \
	MascotaList, MascotaCreate,MascotaUpdate,MascotaDelete

from django.contrib.auth.decorators import login_required

urlpatterns = [
    
    url(r'^$',login_required(index),name='index'),
    #  url(r'^nuevo/',login_required(mascota_crear),name='mascota_crear'),
    #url(r'^listar',login_required(mascota_list),name='mascota_list'),
    #  url(r'^editar/(?P<id_mascota>\d+)/$',login_required(mascota_edit) , name='mascota_edit'),
    # url(r'^eliminar/(?P<id_mascota>\d+)/$',login_required(mascota_delete) , name='mascota_delete'),     

    url(r'^nuevo$', login_required(MascotaCreate.as_view()), name='mascota_crear'),
    url(r'^listar',login_required(MascotaList.as_view()),name='mascota_list'),
    url(r'^editar/(?P<pk>\d+)/$',login_required(MascotaUpdate.as_view()) , name='mascota_edit'),
    url(r'^eliminar/(?P<pk>\d+)/$',login_required(MascotaDelete.as_view()) , name='mascota_delete'),
]
