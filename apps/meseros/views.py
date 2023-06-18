from django.db.models import F
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from rest_framework import status

from apps.meseros.models import Meseros

# Create your views here.
def meseros_list(request):


    data_context = Meseros.objects.filter(nacionalidad='Perú', edad__lt=30)

    return render(request, 'meseros/meseros_list.html', context={'data': data_context})
def meseros_actualizar(request):
    Meseros.objects.all().update(edad=F('edad') + 5)
    data_context = Meseros.objects.all()
    return render(request, 'meseros/meseros_actualizar.html', context={'data': data_context})

class meseros_list_vc(ListView):
    model = Meseros
    template_name = "meseros/meseros_list_vc.html"
    queryset = Meseros.objects.filter(nacionalidad='Perú')

class meseros_crear_vc(CreateView):
    model = Meseros
    fields = ['nombre', 'nacionalidad','edad']
    template_name = 'meseros/meseros_crear_vc.html'
    success_url = reverse_lazy('meseros_list_vc')

class meseros_eliminar_vc(DeleteView):
    model = Meseros
    template_name = 'meseros/meseros_eliminar_vc.html'
    success_url = reverse_lazy('meseros_list_vc')

class meseros_editar_vc(UpdateView):
    model = Meseros
    fields = ['nombre', 'nacionalidad','edad']
    template_name = 'meseros/meseros_editar_vc.html'
    success_url = reverse_lazy('meseros_list_vc')

