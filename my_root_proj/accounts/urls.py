from django.urls import path
from . import views

name = 'accounts'

urlpatterns = [
    path(r'signup', views.shop_signup, name="signup"),
    path(r'login', views.shop_login, name="login"),
]