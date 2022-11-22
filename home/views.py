from django.http import HttpResponse
from django.shortcuts import render
import requests
from django.contrib import messages


# Create your views here.

def home(request):
    
    city=request.GET.get('city','Lucknow')
    try:
        if city is not None:
            url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=11101bf72069781c9f269a7e405cc8ab'
            data=requests.get(url).json()
            print(data)
            payload={
            'city':data['name'], 
            'weather':data['weather'][0]['main'],
            'icon':data['weather'][0]['icon'],
            'kelvin_temperature':data['main']['temp'],
            'celcius_temperature':int(data['main']['temp']-273),
            'pressure':data['main']['pressure'],
            'humidity':data['main']['humidity'],
            'description':data['weather'][0]['description'],
            'error':False
            }
            context={'data':payload}

            print(context)
            return render(request,'home.html',context)
        
    except: 
        context={
            "error":True
        }
        return render(request,'home.html',context)
        # raise ValueError("you haven't entered city name")
        

        
    
    