from django.db import models

from users.models import User


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name="название курса")
    preview = models.ImageField(upload_to="preview/course/%Y/%m/%d/", verbose_name="превью курса")
    description = models.TextField(max_length=1000, verbose_name="описание курса")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses')

    class Meta:
        verbose_name = "курс"
        verbose_name_plural = "курсы"

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=50, verbose_name="название урока")
    description = models.TextField(max_length=500, verbose_name="описание урока")
    preview = models.ImageField(upload_to="preview/lesson/%Y/%m/%d/", verbose_name="превью урока")
    video_url = models.URLField()
    course = models.ForeignKey('Course', on_delete=models.CASCADE, verbose_name="курс", null=True, blank=True, related_name="lessons")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lessons')

    class Meta:
        verbose_name = "урок"
        verbose_name_plural = "уроки"

    def __str__(self):
        return self.name
