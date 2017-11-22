from django.conf.urls import url
from django.contrib.auth.views import login_required

from app.adopcion.views import index_adopcion, SolicitudList, SolicitudCreate, SolicitudUpdate, \
	SolicitudDelete,ListaAdoptantes

urlpatterns = [
    url(r'^index$', index_adopcion),
     url(r'^adoptante/listar$', (ListaAdoptantes.as_view()), name='persona_list'),
    url(r'^solicitud/listar$', login_required(SolicitudList.as_view()), name='solicitud_listar'),
    url(r'^solicitud/nueva$', login_required(SolicitudCreate.as_view()), name='solicitud_crear'),
    url(r'^solicitud/editar/(?P<pk>\d+)$', login_required(SolicitudUpdate.as_view()), name='solicitud_editar'),
    url(r'^solicitud/eliminar/(?P<pk>\d+)$', login_required(SolicitudDelete.as_view()), name='solicitud_eliminar'),
]
