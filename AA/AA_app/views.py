from django.shortcuts import render,redirect,HttpResponse
from .models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.sessions.models import Session

def userindex(request):
    if request.method=="POST":
        name=request.POST['name']
        lastname=request.POST['lname']
        uname=request.POST['uname']
        pwd=request.POST['pwd']      
        phno=request.POST['phno']
        dob=request.POST['dob']
        User.objects.create_user(first_name=name,last_name=lastname,username=uname,password=pwd,Phone_no=phno,DOB=dob) 
        messages.success(request,"registration successfull")
        return render(request,'index.html') 
    else:
        return render(request,'index.html')
    
def login(request):
    if request.method=="POST":
          username = request.POST['uname']
          password = request.POST['pwd']
          user = authenticate(request, username=username, password=password)
          print(user)
          if user is not None and username==username and password==password:
            print(user.id)
            data=user.id
            # login(request, user)
            request.session['user_id']=user.id
            # print('studid')
            return render(request,'uhome.html')
          return HttpResponse("not approved")
    else:
        return render(request,'login.html')

def viewdata(request):
    sid = request.session.get('user_id')
    a=User.objects.get(id=sid)
    print(a)
    print(sid,"sid")
    return render(request,'viewdata.html',{'a':a})

def viewall(request):
    data=User.objects.all()
    return render(request,'viewall.html',{'data1':data})

def nupdate(request,uid):
    if request.method=="GET":
        em=User.objects.get(id=uid)
        return render(request,'nupdate.html',{'em':em})
    elif request.method=="POST":
        n=request.POST['nm']
        a=User.objects.filter(id=uid).update(first_name=n)
        return redirect(viewall)
def ndelete(request,uid):
    a=User.objects.get(id=uid)
    a.delete()
    return redirect(viewall)

