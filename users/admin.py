from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
# from .from import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
# Register your models here.
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
admin.site.register(CustomUser, CustomUserAdmin)