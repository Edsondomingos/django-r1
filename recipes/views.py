from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(
        request,'recipes/pages/home.htm', 
        context={
            'name':'Edson Domingos',
            })

def sobre(request):
    return HttpResponse('<h1>SOBRE - Django</h1>')

def contato(request):
    return HttpResponse('<h1>CONTATO - Django</h1>')