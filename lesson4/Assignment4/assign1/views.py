from django.shortcuts import render
from django.http import HttpResponse, QueryDict
from .forms import UploadFileForm
# Create your views here.
def fileUploadView(request):

    if request.method == 'POST':
        # qdict = QueryDict('', mutable=True)
        # qdict.update({'csrfmiddlewaretoken':request.META['HTTP_X_CSRFTOKEN'],})
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            upload(request.FILES['file'])
            return HttpResponse("<h2>File upload successful!</h2>")
        else:
            return HttpResponse("<h2>File upload not successful!</h2>")
    form = UploadFileForm()
    return render(request, 'fileUploader.html', {'form': form})

def upload(f):
    file = open(f.name, 'wb+')
    for chunk in f.chunks():
        file.write(chunk)