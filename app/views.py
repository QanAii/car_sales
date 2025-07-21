from django.shortcuts import render, redirect
from .models import Car, Category


def index_view(request):
    cars = Car.objects.all()
    return  render(request, 'app/index.html', {'cars':cars})


def detail_views(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, 'app/detail.html', {'car':car})


def create_views(request):
    if request.method == 'POST':
        categories = Category.objects.all()
        title = request.POST.get('title')
        model = request.POST.get('model')
        year = request.POST.get('year')
        price = request.POST.get('price')
        image = request.FILES.get('image')
        category_title = request.POST.get('category')
        category_id = request.POST.get('category')

        category = Category.objects.get(id=category_id)

        Car.objects.create(
            title=title,
            model=model,
            year=year,
            price=price,
            image=image,
            category=category
        )

    return render(request, 'app/create.html')


def update_views(request, car_id):
    car = Car.objects.get(id=car_id)

    if request.method == 'POST':
        car.title = request.POST.get('title')
        car.model = request.POST.get('model')
        car.year = request.POST.get('year')
        car.price = request.POST.get('price')

        category_id = request.POST.get('category')
        car.category = Category.objects.get(id=category_id)

        if request.FILES.get('image'):
            car.image = request.FILES.get('image')

        car.save()
        return redirect('detail', car_id=car.id)

    categories = Category.objects.all()
    return render(request, 'app/update.html', {'car': car, 'categories': categories})


def delete_view(request, car_id):
    car = Car.objects.get(id=car_id)
    car.delete()
    return redirect('index')
