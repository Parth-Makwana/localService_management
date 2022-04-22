from dataclasses import field, fields
from multiprocessing import context
from os import curdir
from pyexpat import model
from re import template
from statistics import mode
from django.shortcuts import redirect, render 
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import customer
from django.contrib.auth import login
from django.views.generic import DetailView,ListView
from django.contrib.auth.views import LoginView
from .forms import CustomerUserCreationForm
from django.urls import reverse_lazy



class View(ListView):
    model = customer
    template_name = 'User/index.html' 

class Createuser(CreateView):
    model=customer
    fields='__all__'
    template_name='User/create_user.html'
    success_url='/User/view'

class Deleteuser(DeleteView):
    model=customer
    success_url='/User/view'

class Updateuser(UpdateView):
    model=customer
    fields='__all__'
    template_name='User/update_user.html'
    success_url='/User/view'

class UserDetail(DetailView):
    model=customer
    template_name='User/user_detail.html'


def index(request):
    return render(request,'index.html')

class UserLogin(LoginView):
    template_name='User/user_login.html'

class SignUpView(CreateView):
    form_class=CustomerUserCreationForm
    success_url=reverse_lazy('User:user_login')
    template_name='User/user_register.html'
    
    


def contact(request):
    return render(request,'User/contact.html')

def categories(request):
    return render(request,'User/category.html')

def listing(request):
    return render(request,'User/listing.html')