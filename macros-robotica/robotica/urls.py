from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crear_robot/', views.crear_robot, name='crear_robot'),
    path('crear_sensor/', views.crear_sensor, name='crear_sensor'),
    path('crear_tarea/', views.crear_tarea, name='crear_tarea'),
    path('buscar_robot/', views.buscar_robot, name='buscar_robot'),
]
