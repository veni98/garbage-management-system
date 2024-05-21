from django.db import models

# Create your models here.
class logins(models.Model):
    name=models.CharField(max_length=50)
    password=models.CharField(max_length=20)

class user(models.Model):
    LOGIN=models.ForeignKey(logins,on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    Email=models.CharField(max_length=50)



    