from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Airtime
from .models import Gfamily
from .models import DAirtime

from .forms import AirtimeForm
import openpyxl

# Create your views here.
#define the http request that a user need to request 
def index(request):
    return render(request, 'airtime/index.html', {
        'airtimes' : Airtime.objects.all()
    })

def view_airtime(request, id):
    airtime = Airtime.objects.get(pk=id)
    return HttpResponseRedirect(reversed('index'))

def upload(request):
    if "GET" == request.method:    
        return render(request, 'airtime/uploadexcel.html', {})
    else:
        excel_file = request.FILES["excel_file"]
        # try put validations here to check extension or file size

    
        #alternative  wb = openpyxl.load_workbook(excel_file)
        wb = openpyxl.load_workbook(excel_file)
        
        worksheet = wb["Sheet1"]
        print(worksheet)

        g_families = []

        # getting value from each cell in row
        for rows in range(2, worksheet.max_row + 1):
            g_names = worksheet.cell(rows, 1).value
            g_ages = worksheet.cell(rows, 2).value
            g_gender = worksheet.cell(rows, 3).value

            g_families.append(Gfamily(name=g_names, age=g_ages, gender=g_gender))
            print(g_families)
        return render(request, 'airtime/uploadexcel.html', { 
            'g_families':g_families,
            'send_airtime' : DAirtime().send()})


def add(request):
    if request.method == 'POST':
        form = AirtimeForm(request.POST)
        if form.is_valid():
            new_airtime_number = form.cleaned_data['airtime_number']
            new_phone_number = form.cleaned_data['phone_number']
            new_amount = form.cleaned_data['amount']
            new_username = form.cleaned_data['username']

            new_airtime = Airtime(
                airtime_number = new_airtime_number,
                phone_number = new_phone_number,
                amount = new_amount,
                username = new_username
            )
                
            new_airtime.save()
            return render(request, 'airtime/add.html', {
                'form' : AirtimeForm(),
                'success': True
            })
    else:
        form = AirtimeForm()
    return render(request, 'airtime/add.html', {
        'form': AirtimeForm()
    })