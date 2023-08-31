from django.http import HttpResponseGone
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponseGone('Hola mundo')
