from django import forms 
from .models import Airtime

class AirtimeForm(forms.ModelForm):
    class Meta:
        model = Airtime
        fields = ['airtime_number', 'phone_number', 'amount','username']
        labels = {
            'airtime_number' : "Airtime Number",
            'phone_number' : "Phone Number",
            'amount' : "Amount",
            'username' : "Username " 
        }
        widgets = {
            'airtime_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'phone_number' : forms.TextInput(attrs={'class': 'form-control'}),
            'amount' : forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'})
        }
        