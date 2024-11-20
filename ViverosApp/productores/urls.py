# productores/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_productores, name='listar_productores'),
    path('registrar/', views.registrar_productor, name='registrar_productor'),
    path('editar/<int:pk>/', views.editar_productor, name='editar_productor'),
    path('eliminar/<int:pk>/', views.eliminar_productor, name='eliminar_productor'),
        # Fincas
    path('fincas/', views.listar_fincas, name='listar_fincas'),
    path('fincas/registrar/', views.registrar_finca, name='registrar_finca'),
    path('fincas/editar/<int:pk>/', views.editar_finca, name='editar_finca'),
    path('fincas/eliminar/<int:pk>/', views.eliminar_finca, name='eliminar_finca'),
    
    # Viveros
    path('viveros/', views.listar_viveros, name='listar_viveros'),
    path('viveros/registrar/', views.registrar_vivero, name='registrar_vivero'),
    path('viveros/editar/<int:pk>/', views.editar_vivero, name='editar_vivero'),
    path('viveros/eliminar/<int:pk>/',views.eliminar_vivero, name='eliminar_vivero'),


    path('labores/', views.listar_labores, name='listar_labores'),
    path('labores/registrar/', views.registrar_labor, name='registrar_labor'),
    path('labores/editar/<int:pk>/', views.editar_labor, name='editar_labor'),
    path('labores/eliminar/<int:pk>/', views.eliminar_labor, name='eliminar_labor'),
]
