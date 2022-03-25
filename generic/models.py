from turtle import update
from django.db import models

# Create your models here.
class BaseField(models.Model):
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    is_deleted=models.BooleanField(default=False)

    class Meta:
        abstract=True