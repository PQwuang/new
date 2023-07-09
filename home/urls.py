from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("introduction", views.introduction,name="introduction"),
    path("bachhoa", views.bachhoa, name="bachhoa"),
    path("dodientu", views.dodientu, name="dodientu"),
    path("trangsuc", views.trangsuc, name="trangsuc"),
    path("sign_in", views.sign_in, name="sign_in"),
    path("register", views.register, name="register"),
]