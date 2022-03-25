from django.shortcuts import render
from django.views.generic import  ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from django.contrib.auth.views import redirect_to_login


# Create your views here.
class BaseListView(LoginRequiredMixin, ListView):
    pass

class BaseDetailView(LoginRequiredMixin,DetailView):
    pass