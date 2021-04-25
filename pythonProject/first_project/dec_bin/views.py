from django.shortcuts import render
import json
from django.http import HttpResponse


# Create your views here.
def binary(request):
    data = json.loads(request.body)
    num = data.get('num')
    n = bin(num)
    return HttpResponse(n)

