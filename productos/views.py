from django.http import HttpResponse
from django.shortcuts import render
from .models import Producto
# Create your views here.

# /productos

def index(request):
    productos = Producto.objects.all()
    print(productos)
    
    return render(
        request,
        'index.html',
        context={'productos': productos}
    )
