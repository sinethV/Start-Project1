
from django.shortcuts import render
from django.http import HttpResponse
from.models import computer
from.models import car

def home(request):
   #add list array for store in class
   comp_Array=computer.objects.all()
   return render(request,'home.html',{'comp_Array':comp_Array})
def home(request):
   car_array=car.objects.all()
   return render(request,'home.html',{'car_array':car_array})

def branch(request):
   return render(request,'branch.html')


# Create your views here.
#first.create obj array.all.obj
#second:pass to html file
#third:html yk file to home for run
