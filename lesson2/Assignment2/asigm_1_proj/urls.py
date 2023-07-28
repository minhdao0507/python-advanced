from . import views
from django.urls import path

app_name = 'asigm_1_proj'
urlpatterns = [
    path('', views.index, name='index'),
    path('/<int:person_id>', views.detail, name='detail' ),
    path('/add_user', views.addUser, name='adduser')
]