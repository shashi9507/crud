from django.shortcuts import render,HttpResponseRedirect
from django.db.models import Q
from .models import Employee

# Create your views here.
def homepage(Request):
    data = Employee.objects.all()
    return render(Request,"Index.html",{"data":data})

def addPage(Request):
    if (Request.method=="POST"):
        e = Employee()
        e.name = Request.POST.get("name")
        e.email = Request.POST.get("email")
        e.Phone = Request.POST.get("Phone")
        e.Designation = Request.POST.get("Designation")
        e.salery = Request.POST.get("Salery")
        e.state = Request.POST.get("State")
        e.city = Request.POST.get("City")
        e.save()
        return HttpResponseRedirect("/")
    return render(Request,"add.html")

def deleteRecord(Request,id):
    try:
        data = Employee.objects.get(id=id)
        data.delete()
    except:
        pass
    return HttpResponseRedirect("/")

def editRecord(Request,id):
    try:
        data = Employee.objects.get(id=id)
        if(Request.method=="POST"):
            data.name = Request.POST.get("name")
            data.email = Request.POST.get("email")
            data.Phone = Request.POST.get("Phone")
            data.Designation = Request.POST.get("Designation")
            data.salery = Request.POST.get("Salery")
            data.state = Request.POST.get("State")
            data.city = Request.POST.get("City")
            data.save()
            return HttpResponseRedirect("/")
        return render(Request,"edit.html",{'data':data})
    except:
        pass 
    return HttpResponseRedirect("/")

def searchPage(Request):
    if(Request.method=="POST"):
        search = Request.POST.get("search")
        data = Employee.objects.filter(Q(name__icontains=search)|Q(city__icontains=search)|Q(email__icontains=search)|Q(state__icontains=search)|Q(Phone__icontains=search)|Q(Designation=search))
        return render(Request,"Index.html",{"data":data}) 
    else:
        return HttpResponseRedirect("/")