from django.urls import path
from Administrador import views

urlpatterns = [
    path('', views.mostrar_index, name='index'),
]