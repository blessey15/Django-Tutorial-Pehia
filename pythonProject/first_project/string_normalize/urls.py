from .views import normalize
from django.urls import path


urlpatterns = [
    path('normalize', normalize, name='norm'),
]

