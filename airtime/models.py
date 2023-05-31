from __future__ import print_function
from django.db import models
import json

import africastalking

# Create your models here.
class Airtime(models.Model):
    airtime_number = models.PositiveIntegerField()
    phone_number = models.CharField(max_length=12)
    amount = models.CharField(max_length=10)
    username = models.CharField(max_length=50)

    def __str__(self):
        return f'Airtime: {self.phone_number}  {self.amount}'
    
"""class DAirtimeMain(models.Model):
    dtree_number = models.AutoField(primary_key=True)
    dtree_date = models.CharField(max_length=50)
    total_amount = models.CharField(max_length=15)
    special_value = models.CharField(max_length=15)

    def __str__(self) -> str:
        return super().__str__()
        """
    
class AirtimeReceive(models.Model):
    airtime_number = models.AutoField(primary_key=True)
    phoneNumber = models.CharField(max_length=15)
    amount = models.CharField(max_length=15) 
    errorMessage = models.CharField(max_length=200)
    status = models.CharField(max_length=20)
    #responses = models.ForeignKey(DAirtimeMain, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'Sent Airtime: {self.phoneNumber}  {self.amount}  {self.errorMessage}'
    

class Gfamily:
    def __init__(self, phoneNumber, amount):
        self.phoneNumber = phoneNumber
        self.amount = amount 
        
    def to_json(self):
        return json.dumps({
            'phoneNumber': self.phoneNumber,
            'amount': self.amount
        })

    @classmethod
    def from_json(cls, s):
        d = json.loads(s)
        return cls(d['phoneNumber'], d['amount'])

    
class DAirtime:
    
    def __init__(self):
        self.username = "muchbeerapi"
        self.api_key = "a2c23698253eafef3f02254cc9c414712ea0cad522ce1bd531ad126c353d959f"

        #initialize the SDK
        africastalking.initialize(self.username, self.api_key)

        #Get the airtime service
        self.airtime = africastalking.Airtime

    def send(self):

        phone_number = "+255757022731"
        amount = "199"
        currency_code = "TZS"

        try:
			# That's it hit send and we'll take care of the rest
            responses = self.airtime.send(phone_number=phone_number, amount=amount, currency_code=currency_code)
            print (responses)
        except Exception as e:
            print (f"Encountered an error while sending airtime:{e}")

if __name__ == '__main__':
    DAirtime().send()

