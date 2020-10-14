from django.shortcuts import render, HttpResponseRedirect
from .forms import FormsStudent
from .models import ModelStudent

# Create your views here.
def add_show(request):
    if request.method == 'POST':
        fs = FormsStudent(request.POST)
        if fs.is_valid():
            fs.save()
            # nm = fs.cleaned_data['name']
            # em = fs.cleaned_data['email']
            # pwd = fs.cleaned_data['password']
            # fd = ModelStudent(name = nm , email = em , password = pwd)
            # fd.save()
            fs = FormsStudent()

    else:
        fs = FormsStudent()    

    stud = ModelStudent.objects.all()
    return render(request , 'enroll/add_show.html' , {'form' : fs , "stu": stud })

def delete_data(request,id):
    if request.method == 'POST':
        pi = ModelStudent.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect("/")

def update_data(request, id):
    if request.method == "POST":
        pi = ModelStudent.objects.get(pk = id)
        fm = FormsStudent(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = ModelStudent.objects.get(pk=id)
        fm = FormsStudent(instance=pi)
    return render(request, 'enroll/updatestu.html' , {'form' : fm}) 