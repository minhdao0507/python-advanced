from django.urls import path
from . import views

app_name = "myproject"
urlpatterns = [
    path('', views.home, name='home'),
    path('<int:id>', views.detail, name='detail'),
    path('login', views.alogin, name='login'),
    path('ahome', views.adminPage, name='ahome'),
]