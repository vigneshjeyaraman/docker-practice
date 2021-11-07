from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager
# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class User(BaseModel, AbstractBaseUser):
    email = models.CharField(max_length=20, null=False, blank=False, unique=True)
    username = models.CharField(max_length=20, null=False, blank=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)
