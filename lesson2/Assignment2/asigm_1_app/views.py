from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    response = HttpResponse()
    response.write("<h1>This is my first Django application</h1>")
    return response