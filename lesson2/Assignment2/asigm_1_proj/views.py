from unicodedata import name
from django.shortcuts import render
from .models import Person
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from .forms import AddUser
from django.contrib import messages
# Create your views here.

def index(request):
    person_list = Person.objects.all()
    template = loader.get_template('index.html')
    context = {
        'person_list': person_list
    }
    return HttpResponse(template.render(context, request))

def detail(request, person_id):
    try:
        person = Person.objects.get(pk=person_id)
    except Person.DoesNotExist:
        raise Http404("Person doesn't not exist")
    return render(request, 'detail.html', {'person':person})

def addUser(request):
    newUser = AddUser()
    if request.method == 'POST':
        newUser = Person(name = request.POST['name'], age=request.POST['age'],address=request.POST['address'],mobile_number=request.POST['mobile_number'] )
        if newUser.name != '':
            newUser.save()
            messages.info(request, 'Add user successfully!')
            return HttpResponseRedirect('/asigm_1_proj')
    
    return render(request, 'add.html', {'form': newUser})
