from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from app.mascota.forms import MascotaForm
from app.mascota.models import Mascota

def index(request):
    return render(request,'mascota/index.html')
    
#fucncion para crear
def mascota_crear(request):
    	if request.method == 'POST':
		form = MascotaForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('mascota:mascota_list')
	else:
		form = MascotaForm()
	return render(request, 'mascota/mascota_crear.html', {'form':form})
	
#fucncion para listar
def mascota_list(request):
	mascota = Mascota.objects.all().order_by('id')
	contexto = {'mascotas':mascota}
	return render(request, 'mascota/mascota_list.html', contexto)
#fucncion para editar
def mascota_edit(request, id_mascota):
	mascota = Mascota.objects.get(id=id_mascota)
	if request.method == 'GET':
		form = MascotaForm(instance=mascota)
	else:
		form = MascotaForm(request.POST, instance=mascota)
		if form.is_valid():
			form.save()
		return redirect('mascota:mascota_list')
	return render(request, 'mascota/mascota_crear.html', {'form':form})

#fucncion para eliminar
def mascota_delete(request, id_mascota):
	mascota = Mascota.objects.get(id=id_mascota)
	if request.method == 'POST':
		mascota.delete()
		return redirect('mascota:mascota_list')
		
	return render(request, 'mascota/mascota_delete.html', {'mascota':mascota})

#vistas con clases listar
class MascotaList(ListView):
	model = Mascota
	template_name='mascota/mascota_list'
	paginate_by =0
#clase para crear 
class MascotaCreate(CreateView):
	model = Mascota
	form_class = MascotaForm
	template_name = 'mascota/mascota_crear.html'
	success_url = reverse_lazy('mascota:mascota_list')
#clase para actualizar
class MascotaUpdate(UpdateView):
	model = Mascota
	form_class = MascotaForm
	template_name = 'mascota/mascota_crear.html'
	success_url = reverse_lazy('mascota:mascota_list')
#clase para eliminar
class MascotaDelete(DeleteView):
	model=Mascota
	template_name='mascota/mascota_delete.html'
	success_url = reverse_lazy('mascota:mascota_list')

