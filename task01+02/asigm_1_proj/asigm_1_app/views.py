from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
from django.template import loader
from .forms import RegisterForm
from django.contrib.auth.models import User

# Create your views here.

# def index(request):
#     response = HttpResponse()
#     response.write("<h1>Welcome</h1>")
#     response.write("This is my first Django application")
#     return response

def index(request):
    person_list = Person.objects.all()
    template = loader.get_template('index.html')
    context = {
        'person_list':person_list,
    }
    return HttpResponse(template.render(context,request))

def detail(request,id):
    template = loader.get_template('detail.html')
    person = Person.objects.get(id=id)
    context = {
        'person':person,
    }
    return HttpResponse(template.render(context,request))

def register(request):
    if request.method == 'POST':
        response = HttpResponse()

        # new_user = User(username=request.POST['username'], 
        # email=request.POST['email'],
        # is_user = True,
        # is_staff = True)
        # new_user.set_password(request.POST['password'])
        # new_user.save()

        response.write("<hi>Thanks for registering</h1><br>")
        response.write("Your username:"+ request.POST['username']+ "</br>")
        response.write("Your email:" + request.POST['email'] + "</br>")
        return response

    registerForm = RegisterForm()
    return render(request,'register.html',{'form':registerForm})