from django.shortcuts import render,redirect
from .models import*

# Create your views here.

def Index(request):
    return render(request,"register.html")

def Showdata(request):
    a=Student.objects.all()
    return render(request,"show.html")  



def Update(request,id):
    e = Student.objects.filter(id=id)
    if e.count() > 0:
        e.update(
            name= request.POST['name'], 
            email= request.POST['email'], 
            mobile_no = request.POST['mobile_no'], 
            address= request.POST['address'], 
            courses = request.POST['courses'], 
        
        )
    return redirect("showdata")


def Editpage(request,pk):
    c = Student.objects.get(id=pk)
    return render(request,"update.html",{'user':c})

def Deletedata(request,id):
    b = Student.objects.get(id=id)
    b.delete()
    return redirect("showdata")      


def Register(request):
    if request.method=="POST":

     
        name = request.POST['name']
        email = request.POST['email']
        mobile_no=request.POST['mobile_no']
        address = request.POST['address']
        courses=request.POST['courses']
      


        std = Student.objects.create(name =name,
                                    email =email,
                                    mobile_no=mobile_no,
                                    address=address,
                                    courses=courses,
                                )

    return redirect("showdata")      

