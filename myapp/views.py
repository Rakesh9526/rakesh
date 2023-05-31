from django.shortcuts import render,redirect
from myapp.models import studentdata
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage

# Create your views here.


def studentdb(request):
    return render(request,"students.html")



def savestudent(req):
    if req.method == "POST":
        n = req.POST.get('name')
        a = req.POST.get('age')
        m = req.POST.get('mobile')
        im = req.FILES['img']
        obj = studentdata(Name=n,Age=a,Mobile_number=m,Image=im)
        obj.save()
        return redirect(studentdb)



def displaydata(req):
    data =studentdata.objects.all()
    return render(req,"displaydata.html",{'data':data})



def editpage(req,dataid):
    data = studentdata.objects.get(id=dataid)
    return render(req,"editpage.html",{'data':data})


def updatestudent(req,dataid):
    if req.method =="POST":
        na = req.POST.get('name')
        a = req.POST.get('age')
        m = req.POST.get('mobile')
        try:
            im = req.FILES['img']
            fs = FileSystemStorage()
            file = fs.save(im.name,im)

        except MultiValueDictKeyError:
            file = studentdata.objects.get(id=dataid).Image
        studentdata.objects.filter(id=dataid).update(Name=na,Age=a,Mobile_number=m,Image=file)
        return redirect(displaydata)


def deletestudent(req,dataid):
    data =studentdata.objects.filter(id=dataid)
    data.delete()
    return redirect(displaydata)

