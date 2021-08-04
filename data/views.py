from django.shortcuts import render
from django.http import response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import datetime
from .models import date_time
import pytz

@csrf_exempt
def index(request):
    
    if request.method == 'POST':

        data = request.POST['data']
        print(data)
        if data == 'ON' or data == 'OFF':
            tz_NY = pytz.timezone('Asia/Kolkata')
            x = datetime.datetime.now(tz_NY)

            time = x.strftime("%X")
            date = x.strftime("%x")
            print(date, time)
            print(type(date), type(time))
            obj = date_time(dat = date, tim = time, status = data)
            obj.save()
            return HttpResponse("It works! :)")

        return HttpResponseRedirect(reverse('home'))

    return render(request, 'index.html')
            
def table(request):
    details=date_time.objects.all()
    return render(request, 'table_view.html',{'details':details})
