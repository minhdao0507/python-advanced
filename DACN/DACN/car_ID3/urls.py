from unicodedata import name
from django.urls import path
from . import views
app_name="car_ID3"
urlpatterns =[
    path('admin', views.index, name='index'),
    path('admin/home',views.adminPage, name='admin-home'),
    path('', views.homePage, name='home')
]