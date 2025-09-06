from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required 

@login_required(login_url='/login/')
def today_task(request):
    if request.method=='POST':
        data=request.POST
        a=data.get('task_name')
        b=data.get('task_status')
        c=data.get('task_discription')
        


        Task.objects.create(
            task_name=a,
            task_status=b,
            task_discription=c

        
    )
        
        return redirect('/task')
    queryset=Task.objects.all()
    context={'Task':queryset}
    return render(request, 'tasks.html',context)




@login_required(login_url='/login/')
def delete(request, id):
    queryset=Task.objects.get(id = id)
    queryset.delete()
        
    return redirect('/task')

@login_required(login_url='/login/')
def update(request,id):
    queryset=Task.objects.get(id = id)
    if request.method == 'POST':
        data = request.POST

        
        a = data.get("task_name")

        b = data.get('task_status')
        c = data.get('task_discription')
        if a:
            queryset.task_name=a
        if b:
            queryset.task_status=b
        if c:
            queryset.task_discription=c
        queryset.save()
      
        
        return redirect('/task')
    
    context={'task':queryset}

    return render(request ,'update_today.html',context)


def login_page(request):
    if request.method == 'POST':
        data = request.POST
        username=data.get('username')
        password=data.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request,'invalid username')
            return redirect('/login/')
        
        user=authenticate(username=username,password=password)
        if user is None:
            messages.error(request,'invalid username or password')
            return redirect('/login/')

        else:
            login(request,user)
            return redirect('/task/')





    return render(request,'login.html')
    
def logout_page(request):
    logout(request)
    return redirect('/login/')





def register(request):
    if request.method == 'POST':
        data = request.POST


        
        first=data.get('first_name')
        last=data.get('last_name')
        username=data.get('Username')
        password=data.get('password')

        user=User.objects.filter(username=username)
        if user.exists():
            messages.error(request,'username is already taken')
            return redirect('/register/')

        user=User.objects.create(
           first_name =first,
           last_name=last,
           username=username,
                            )
        user.set_password(password)
        user.save()


        messages.info(request,'Account created successfully')

        return redirect('/register/')
    
    return render(request,'register.html')

