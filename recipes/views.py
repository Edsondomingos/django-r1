from django.shortcuts import render
from utils.recipes.factory import make_recipe

# Create your views here.
# HTTP Request

def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'recipes': [make_recipe() for _ in range(3)],
        'home': True
    })
 
def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipes': make_recipe(),
        'id': id,
    })

def contact(request, id):
    return render(request, 'recipes/pages/contact-view.html', context={
        'recipes': make_recipe(),
    })
