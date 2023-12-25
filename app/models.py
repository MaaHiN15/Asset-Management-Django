from django.db import models

# Create your models here.

class User(models.Model):
    id = models.UUIDField(primary_key=True, unique=True)
    emp_no = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone_no = models.IntegerField()
    password = models.CharField(max_length=50)
    class Meta:
        db_table = 'user'
    

    

