from django.db import models

# Create your models here.
class Airtime(models.Model):
    airtime_number = models.PositiveIntegerField()
    phone_number = models.CharField(max_length=12)
    amount = models.CharField(max_length=10)
    username = models.CharField(max_length=50)

    def __str__(self):
        return f'Airtime: {self.phone_number}  {self.amount}'
    
class Gfamily:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age 
        self.gender = gender