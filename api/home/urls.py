from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='home'),
    path('post_todo/', views.post_todo, name='home'),
    path('get_todo/', views.get_todo, name='home'),


]
