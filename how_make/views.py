from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'how_make/pages/home.htm', 
        context={
            'name':'Edson Domingos',
            'titulo': 'Hamburguer Especial com Batara Frita',
            'data': '20/01/2023',
            'profissao': 'Desenvolvedor',
            'email': 'edson@email.com',
            'social': '@EdsonDoming0s',
            'ingredientes': [
                'Pão de Hamburguer',
                'Tomate',
                'Alface',
                'Queijo Cheddar',
                'Carne moida de primeira'
            ],
            'preparo': [
                'Corte 1 tomate em rodelas',
                'Separe uma folha de alface',
                'Frite a carne moide após temperar e ir dando forma',
                'Monte o Hamburguer de baixo para cima'
            ],
            'img':'/imgs/burguer2.png'
        })
