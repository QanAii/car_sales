from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Car, Category
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError

User = get_user_model()


def index_view(request):
    cars = Car.objects.all()
    return  render(request, 'app/index.html', {'cars':cars})


def detail_view(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
    except Car.DoesNotExist:
        messages.error(request, "Автомобиль не найден"),
        return render(request, 'app/detail.html')
    return render(request, 'app/detail.html', {'car': car})


def create_view(request):
    if not request.user.is_authenticated:
        messages.error(request, "Сначала войдите в аккаунт.")
        return redirect('login')

    if request.method == 'POST':
        title = request.POST.get('title')
        model = request.POST.get('model')
        year = request.POST.get('year')
        price = request.POST.get('price')
        image = request.FILES.get('image')
        category_id = request.POST.get('category')

        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            messages.error(request,"Категория не найдена.")
            return redirect('create')

        new_car = Car(
            title=title,
            model=model,
            year=year,
            price=price,
            image=image,
            category=category,
            user=request.user
        )
        new_car.save()

        messages.success(request, "Объявление успешно создано!")
        return redirect('index')

    categories = Category.objects.all()
    return render(request, 'app/create.html', {'categories': categories})


def update_view(request, car_id):
    car = Car.objects.get(id=car_id)

    if request.method == 'POST':
        car.title = request.POST.get('title')
        car.model = request.POST.get('model')
        car.year = request.POST.get('year')
        car.price = request.POST.get('price')
        category_id = request.POST.get('category')

        car.category = Category.objects.get(id=category_id)

        if request.FILES.get('image'):
            car.image = request.FILES['image']

        car.save()

        messages.success(request, "Объявление обновлено!")
        return redirect('detail', car_id=car.id)

    categories = Category.objects.all()
    return render(request, 'app/update.html', {'car': car, 'categories': categories})


def delete_view(request, car_id):
    car = Car.objects.get(id=car_id)

    if request.method == 'POST':
        car.delete()
        return redirect('index')

    return render(request, 'app/delete.html', {'car':car})


def register_view(request):
    errors = []

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        if not username:
            errors.append("Введите имя пользователя")
        if not password:
            errors.append("Введите пароль")

        if User.objects.filter(username=username).exists():
            errors.append("Пользователь с таким именем уже существует")

        # Проверка сложности пароля по настройкам
        try:
            password_validation.validate_password(password)
        except ValidationError as e:
            errors.extend(e.messages)

        if not errors:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)  # Логиним пользователя сразу после регистрации
            messages.success(request, "✅ Регистрация прошла успешно!")
            return redirect('index')

    return render(request, 'app/register.html', {'errors': errors})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username').strip()
        password = request.POST.get('password').strip()

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            messages.success(request, f"Добро пожаловать, {user.username}!")
            return redirect('index')
        else:
            messages.error(request, 'Неверные данные для входа.')

    return render(request, 'app/login.html')


def logout_view(request):
    logout(request)
    messages.info(request, "Вы вышли из аккаунта.")
    return redirect('index')
