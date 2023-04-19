from django.shortcuts import render,redirect
from .models import Student
from django.contrib import messages

def home(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        address = request.POST['address']
        if Student.objects.filter(email=email).exists():
            messages.warning(request, "Email Already Registered")
        elif Student.objects.filter(contact=contact).exists():
            messages.warning(request, "Contact Already Registered")
        else:
            student = Student.objects.create(name=name,
                               email=email,
                               contact=contact,
                               address=address)
            student.save()
        return redirect('/')

    else:
        students=Student.objects.all()
        return render(request,"home.html", {'students':students})


def delete(request,st_id):
    st = Student.objects.filter(id=st_id)
    st.delete()
    return redirect('/')

def update(request, st_id):
    obj = Student.objects.get(id=st_id)
    if request.method=='POST':
        obj.name = request.POST['name']
        obj.email = request.POST['email']
        obj.contact = request.POST['contact']
        obj.address = request.POST['address']
        obj.save()
        return redirect('/')
    else:
        return render(request,'update.html',{'student':obj})

