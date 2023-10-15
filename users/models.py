from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
class CustomUser(AbstractUser):
    sex_choice =((0,"nữ"),(1,"nam"),(2,"ko xác định"))
    age = models.IntegerField(default=0)
    sex = models.IntegerField(choices=sex_choice, default=2)
    address = models.CharField(default="", max_length=255)

