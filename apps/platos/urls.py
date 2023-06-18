from django.urls import path
from . import views

urlpatterns = [
    path('platos_list/', views.platos_list, name='platos_list'),
    path('platos_list_srl/', views.platos_list_srl, name='platos_list_srl'),
]
