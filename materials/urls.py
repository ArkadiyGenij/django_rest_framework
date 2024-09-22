from django.urls import path, include
from rest_framework.routers import DefaultRouter
from setuptools.extern import names

from materials.apps import MaterialsConfig
from materials.views import CourseViewSet, LessonListCreateView, LessonRetrieveUpdateDestroyView

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
    path('', include(router.urls)),
    path('lessons/', LessonListCreateView.as_view(), name='lessons-list-create'),
    path('lessons/<int:pk>/', LessonRetrieveUpdateDestroyView.as_view(), name='lessons-detail')
]
