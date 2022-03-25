from django.contrib import admin

from .models import customer, serviceprovider

admin.site.register(customer)
admin.site.register(serviceprovider)