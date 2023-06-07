from django.shortcuts import render
from platos.models import Platos

# Create your views here.
def platos_list(request):

    Platos.objects.create(nombre='Rocoto Relleno', procedencia='Perú', precio=45)
    Platos.objects.create(nombre='Ají de Gallina', procedencia='Perú', precio=50)
    Platos.objects.create(nombre='Papa a la Huancaína', procedencia='Perú', precio=35)

    data_context = Platos.objects.filter(procedencia='Perú', precio__gt=40)

    return render(request, 'platos/platos_list.html', context={'data': data_context})
