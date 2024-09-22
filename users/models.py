from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="почта")
    phone_number = models.CharField(max_length=30, verbose_name="номер телефона")
    city = models.CharField(max_length=100, verbose_name="город")
    avatar = models.ImageField(upload_to="avatar/", verbose_name="аватар", blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"

    def __str__(self):
        return self.email
