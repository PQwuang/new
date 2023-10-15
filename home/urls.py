from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView #new
urlpatterns = [
    path("", views.dodientu, name="dodientu"),
    path("about", views.about, name="about"),
    path("introduction", views.introduction,name="introduction"),
    path("bachhoa", views.bachhoa, name="bachhoa"),
    path("dodientu", views.dodientu, name="dodientu"),
    path("trangsuc", views.trangsuc, name="trangsuc"),
    # path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),#new
    path("editprofile", views.editprofile, name="editprofile"),
    path("sign_up", views.sign_up, name="sign_up"),
    # path("password_change_form", views.password_change_form, name="password_change_form"),
]
