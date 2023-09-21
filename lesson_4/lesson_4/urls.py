from django.contrib import admin
from django.urls import path, include

from app_lesson_4.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lesson_4/', index),
]
