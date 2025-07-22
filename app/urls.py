from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('register/', views.register_view, name='register'),
    path('car/<int:car_id>/', views.detail_view, name='detail'),
    path('create/', views.create_view, name='create'),
    path('update/<int:car_id>/', views.update_view, name='update'),
    path('delete/<int:car_id>/', views.delete_view, name='delete'),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
