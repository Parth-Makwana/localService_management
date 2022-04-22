from .models import customer,serviceprovider,Customeruser
from django import forms
from django.contrib.auth.forms import UserCreationForm

class CustomerUserCreationForm(UserCreationForm):
    model=Customeruser
    fields=['username','email','password1','password2']
    template_name='User/register.html'