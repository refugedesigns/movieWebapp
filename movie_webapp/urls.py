from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('update/<str:movie_id>/', views.update, name='update'),
    path('delete/<str:pk>/', views.delete, name='delete'),
]
