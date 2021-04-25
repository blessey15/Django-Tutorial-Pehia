from django.shortcuts import render
import json
from django.http import HttpResponse


# Create your views here.
def normalize(request):
    data = json.loads(request.body)
    text = data.get('text')
    return HttpResponse(text.lower())
