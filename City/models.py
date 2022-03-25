from django.db import models
from django.test import TransactionTestCase

# Create your models here.
class state(models.Model):
    StateName=models.CharField(max_length=30)

    class Meta():
        db_table='State'

class city(models.Model):
    StateId=models.ForeignKey(state,on_delete=models.CASCADE)
    CityName=models.CharField(max_length=30)

    class Meta():
        db_table='City'

class service(models.Model):
    ServiceName=models.CharField(max_length=50)

    class Meta():
        db_table='Service'

class payment(models.Model):
    Amount=models.IntegerField()
    Transaction=models.CharField(max_length=20)

    class Meta():
        db_table='Payment'
