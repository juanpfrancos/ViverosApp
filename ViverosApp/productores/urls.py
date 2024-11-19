# productores/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_productores, name='listar_productores'),
    path('registrar/', views.registrar_productor, name='registrar_productor'),
    path('editar/<int:pk>/', views.editar_productor, name='editar_productor'),
    path('eliminar/<int:pk>/', views.eliminar_productor, name='eliminar_productor'),
]
