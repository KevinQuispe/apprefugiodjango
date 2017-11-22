from django.contrib import admin
from app.adopcion.models import Persona
# Register your models here.
# class ListaAdmin(admin.ModelAdmin):
#     list_display=('nombre')

admin.site.register(Persona)