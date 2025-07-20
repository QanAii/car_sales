from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('car/<int:car_id>/', views.detail_views, name='detail'),
]
