from .views import binary
from django.urls import path

urlpatterns = [
    path('binary', binary, name='bin'),
]
