from django.urls import path
from . import views

name = 'accounts'

urlpatterns = [
    path(r'signup', views.signup, name="signup"),
    path(r'login', views.login, name="login"),
]