from django.shortcuts import get_object_or_404, render, redirect
from .models import * 
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
# from .forms import ProfileUpdateForm
from django.contrib.auth.decorators import login_required

#SEARCH IMPORTS
from django.db.models import Q
from django.views.generic import TemplateView, ListView


# Application views.
@login_required(login_url='/login')
def home(request):
    posts= Post.objects.all()
    return render(request, 'index.html', {'posts':posts})


def register(request):
    if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2= request.POST['password2']
        
        if password1 != password2:
            messages.error(request,"confirm your passwords")
            return redirect('/register')
        
        new_user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
        
        new_user.save()
        return redirect ("login") 
    return render(request, 'register.html')


def user_login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']  
        
        user = authenticate (request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Welcome , you are now logged in")
            return redirect ("home")
    return render(request, 'login.html')

@login_required(login_url='/login')
def user_logout(request):
    logout(request)
    return render(request, 'index.html')

#user_profile
@login_required(login_url='/login')

def user_profile(request):
    users= User.objects.all()
    current_user = request.user
    user_posts = Post.objects.filter(person=current_user)
    print(user_posts)
    
    return render (request, 'profile.html', {'users':users, 'user_posts':user_posts})


@login_required(login_url='/login')