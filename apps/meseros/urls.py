from django.urls import path
from . import views

urlpatterns = [
    path('meseros_list/', views.meseros_list, name='meseros_list'),
    path('meseros_actualizar/', views.meseros_actualizar, name='meseros_actualizar'),
    path('meseros_list_vc/', views.meseros_list_vc.as_view(), name='meseros_list_vc'),
    path('meseros_crear_vc/', views.meseros_crear_vc.as_view(), name='meseros_crear_vc'),
    path('meseros_eliminar_vc/<int:pk>/', views.meseros_eliminar_vc.as_view(), name='meseros_eliminar_vc'),
    path('meseros_editar_vc/<int:pk>/', views.meseros_editar_vc.as_view(), name='meseros_editar_vc'),
]
