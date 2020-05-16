from django.urls import path
from . import views

name = 'site'

urlpatterns = [
    path(r'index', views.index, name="index"),
]