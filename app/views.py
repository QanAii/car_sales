from django.shortcuts import render
from .models import Car

def index_view(request):
    cars = Car.objects.all()
    return  render(request, 'app/index.html', {'cars':cars})

def detail_views(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, 'app/detail.html', {'car':car})

