from django.shortcuts import render
from .models import Trabajo 
# Create your views here.
def Home(request):
    
    return render(request, 'home.html')

def Nosotros(request):

    return render(request, 'nosotros.html')

def Valores(request):
    
    return render(request, 'valores.html')

def Trabajos(request):
    
    nuevos = Trabajo.objects.all()

    return render(request, 'trabajos.html', {'nuevo':nuevos})

def Equipo(request):
    
    return render(request, 'equipo.html')

def Contacto(request):
    
    return render(request, 'contacto.html')

def Tienda(request):
    
    return render(request, 'tienda.html')