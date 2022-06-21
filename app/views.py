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

