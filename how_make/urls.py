from django.urls import path
from how_make.views import home

urlpatterns = [
    path('', home),
]
