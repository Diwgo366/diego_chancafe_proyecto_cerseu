from django.db.models import F
from django.shortcuts import render
from meseros.models import Meseros

# Create your views here.
def meseros_list(request):


    data_context = Meseros.objects.filter(nacionalidad='Perú', edad__lt=30)

    return render(request, 'meseros/meseros_list.html', context={'data': data_context})
def meseros_actualizar(request):
    Meseros.objects.all().update(edad=F('edad') + 5)
    data_context = Meseros.objects.all()
    return render(request, 'meseros/meseros_actualizar.html', context={'data': data_context})