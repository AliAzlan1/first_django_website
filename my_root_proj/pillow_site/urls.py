from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path(r'', views.pillowsite_index, name="pillow_index"),
]