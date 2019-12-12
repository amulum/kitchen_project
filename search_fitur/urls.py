from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'search_fitur'
urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),

]