from django.db import models
from django.contrib.auth.models import AbstractUser


class customer(models.Model):
    CustomerName=models.CharField(max_length=30)
    address=models.CharField(max_length=70)
    StateId=models.IntegerField()
    CityId=models.IntegerField()
    Pincode=models.IntegerField()
    ContactNumber=models.CharField(max_length=11)

    class Meta():
        db_table='customer'

class serviceprovider(models.Model):
    ServiceName=models.CharField(max_length=30)
    address=models.CharField(max_length=70)
    StateId=models.IntegerField()
    CityId=models.IntegerField()
    UserId=models.IntegerField()
    Pincode=models.IntegerField()
    ContactNumber=models.CharField(max_length=11)

    class Meta():
        db_table='service_provider'

class Customeruser(AbstractUser):
    pass

    class Meta():
        db_table='customer_user'
def __str__(self):
    return self.username

    
