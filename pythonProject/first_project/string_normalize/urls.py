from .views import normalize, fetch, display
from django.urls import path


urlpatterns = [
    path('fetch', fetch, name='fetch'),
    path('normalize', normalize, name='norm'),
    path('display', display, name='display')
]

