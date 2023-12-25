from django.db import models
import uuid

def get_uuid():
    return uuid.uuid4().hex[-8:]


class User(models.Model):
    id = models.CharField(primary_key=True, unique=True, default=get_uuid, max_length=8)
    emp_no = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone_no = models.IntegerField()
    password = models.CharField(max_length=50)
    class Meta:
        db_table = 'user'
    

class Label(models.Model):
    id = models.CharField(primary_key=True, unique=True, default=get_uuid, max_length=8)
    name = models.CharField(max_length=100)
    class Meta:
        db_table = 'Label'

