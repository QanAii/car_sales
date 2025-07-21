from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('car/<int:car_id>/', views.detail_views, name='detail'),
    path('create/', views.create_views, name='create'),
    path('update/<int:car_id>/', views.update_views, name='update'),
    path('delete/<int:car_id>/', views.delete_view, name='delete'),
]
