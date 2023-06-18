from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated

from apps.platos.models import Platos

# Create your views here.
def platos_list(request):

    Platos.objects.create(nombre='Rocoto Relleno', procedencia='Perú', precio=55)
    Platos.objects.create(nombre='Ají de Gallina', procedencia='Perú', precio=50)
    Platos.objects.create(nombre='Papa a la Huancaína', procedencia='Perú', precio=35)

    data_context = Platos.objects.filter(procedencia='Perú', precio__gt=40)

    return render(request, 'platos/platos_list.html', context={'data': data_context})

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def platos_list_srl(request):

    lista = serializers.serialize('json', Platos.objects.filter(precio__gt=50), fields=["nombre","precio","procedencia"])
    return HttpResponse(lista, content_type='application/json')