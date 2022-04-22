from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import  UserCreationForm
from .models import Customeruser, customer, serviceprovider

admin.site.register(customer)
admin.site.register(serviceprovider)

class CustomerUserAdmin(UserAdmin):
    add_form = UserCreationForm
    model = Customeruser
    list_display = ['username', 'email', 'is_staff', 'is_active']
    
admin.site.register(Customeruser, CustomerUserAdmin)