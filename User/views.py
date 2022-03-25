from dataclasses import field, fields
from multiprocessing import context
from os import curdir
from pyexpat import model
from re import template
from statistics import mode
from django.shortcuts import render 
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import customer
from django.views.generic import DetailView,ListView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm


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

def register(request):

    form=UserCreationForm
    return render(request,'User/user_register.html',{'form':form})
    redirect("login")

