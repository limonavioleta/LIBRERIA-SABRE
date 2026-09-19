from django.shortcuts import render
from Administrador.models import *
# Create your views here.
def mostrar_index(request):

    return render(request, 'Administrador/index.html')
