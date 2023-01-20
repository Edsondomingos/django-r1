from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# HTTP Request
def home(request):
    # HTTP Response
    return render(request, 'recipes/pages/home.html', context={'name': 'Eberton Marinho'})
 
def sobre(request):
    # HTTP Response
    return HttpResponse('<h1>SOBRE - DJANGO</h1>')

def contato(request):
    # HTTP Response
    return HttpResponse('<h1>CONTATO - Django</h1>')
