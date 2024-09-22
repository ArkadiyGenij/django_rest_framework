from django.contrib.auth.models import AbstractUser
from django.db import models

from materials.models import Course, Lesson


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


class Payments(models.Model):
    PAYMENT_METHOD = [
        ('cash', 'наличные'),
        ('translation', 'перевод на счет')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="payments")
    payment_date = models.DateField(auto_now_add=True)
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True, related_name="paid_course")
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True, blank=True, related_name="paid_lesson")
    payment_amount = models.IntegerField(default=0)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD)

    class Meta:
        verbose_name = "платеж"
        verbose_name_plural = "платежи"
