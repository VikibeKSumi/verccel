from django.urls import path
from . import views


app_name = 'appv'

urlpatterns = [
    path('', views.home, name='home')
]