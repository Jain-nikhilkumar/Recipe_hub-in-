from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    roll=models.IntegerField()
    city=models.CharField(max_length=100)
    marks=models.IntegerField()
    

class product(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    description=models.TextField()
    image=models.ImageField(upload_to='product/images')
    
class Car(models.Model):
    car_name=models.CharField(max_length=100)
    car_speed=models.IntegerField(default=50)
    
    def __str__(self):
        return self.car_name 
    