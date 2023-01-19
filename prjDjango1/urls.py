"""prjDjango1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from recipes.views import home, sobre, contato

def my_view(request):
    # HTTP RESPONSE
    return HttpResponse('<h1>Hello Django</h1>')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls')),
    path('how_make/', include('how_make.urls')),
    path('home/', home),
    path('sobre0/', my_view),
    path('sobre01/', sobre),
    path('contato0/', contato),
]
