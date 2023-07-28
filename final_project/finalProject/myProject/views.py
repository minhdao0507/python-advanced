from django.shortcuts import render
from .models import myProject, User
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse, HttpResponseForbidden
import json
from .forms import proForm
# Create your views here.

def home(request):
    pro_list = myProject.objects.filter(status='Active').values()
    return render(request, "home.html",{'pro_list': pro_list})

def detail(request, id):
    my_project = myProject.objects.filter(id=id).values()
    return render(request, "project1.html",{'my_project': my_project[0]})

def alogin(request):
    request.session['islogin'] = False
    if request.method =='POST':
        user_from_post = json.load(request)['user']
        user = User.objects.get(username=user_from_post['username'])
        if (check_password(user_from_post['password'],user.password)):
            request.session['islogin'] = True
            return HttpResponse('')
        return HttpResponseForbidden('')
    return render(request, 'login.html')

def adminPage(request):
    islogin = request.session.get('islogin', False)
    request.session.set_expiry(300)
    if islogin:
        pro_list = myProject.objects.all().values()
        if request.method=='POST':
            name=request.POST.get('name')
            id = request.POST.get('id')
            search = request.POST.get('insearch')
            if name:
                fpro = myProject.objects.filter(name=name).values()
                if fpro:
                    fpro.update(about_pro = request.POST.get('about_pro'),tech_used= request.POST.get('tech_used'),source = request.POST.get('source'),status = request.POST.get('status'))
                    pro_list = myProject.objects.all().values()
                else:
                    form = proForm(request.POST)
                    if form.is_valid():
                        form.save()
                        pro_list = myProject.objects.all().values()
            elif id:
                fpro = myProject.objects.filter(id=id)
                fpro.delete()
                pro_list = myProject.objects.all().values()
            elif search:
                pro_list = myProject.objects.filter(name__contains = search).values()
        return render(request,'admin.html', {'pro_list': list(pro_list)})

    return render(request, 'login.html')
