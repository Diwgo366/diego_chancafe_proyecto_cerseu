from django.urls import path
from . import views

urlpatterns = [
    path('meseros_list/', views.meseros_list, name='meseros_list'),
    path('meseros_actualizar/', views.meseros_actualizar, name='meseros_actualizar'),
]
