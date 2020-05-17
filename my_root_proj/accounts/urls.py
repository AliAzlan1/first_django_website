from django.urls import path
from . import views

name = 'accounts'

urlpatterns = [
    path(r'signup', views.shop_signup, name="signup"),
    path(r'login', views.shop_login, name="login"),
    path(r'logout', views.shop_logout, name="logout"),
    path(r'account_activation_sent', views.account_activation_sent, name='account_activation_sent'),
    path(r'activate/<uidb64>/<token>',views.activate, name='activate'),
    #path(r'activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})',views.activate, name='activate'),
]