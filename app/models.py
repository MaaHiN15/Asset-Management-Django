from django.db import models

# Create your models here.

class Customer(models.Model):
    id = models.UUIDField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=50)
    class Meta:
        db_table = 'customer'