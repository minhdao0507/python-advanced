from django.shortcuts import render
from .models import Animal
from .forms import AnimalForm
from django.http import HttpResponse
# Create your views here.

def addAnimal(req):
    if req.method == 'POST':
        form = AnimalForm(req.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h2>Create successful!</h2>")
        else:
            return HttpResponse("<h2>Create not successful!</h2>")
    
    form = AnimalForm()
    return render(req, 'form.html', {'form': form})