from django.urls import path
from . import views

appname = 'assign2'
urlpatterns = [
    path('', views.addAnimal),
]