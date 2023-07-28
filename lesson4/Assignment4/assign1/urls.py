from django.urls import path
from . import views

appname = 'file_uploader'
urlpatterns = [
    path('', views.fileUploadView, name='fileupload'),
]