from django.shortcuts import render
import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import SampleTable


# Create your views here.
@csrf_exempt
def fetch(request):
    data = json.loads(request.body)
    name = data.get('name')
    mail = data.get('mail')
    about = data.get('about')
    d = SampleTable.objects.create(name=name, mail=mail, about=about)
    d.save()
    return HttpResponse('Data added')


def display(request):
    dat = list(SampleTable.objects.values())
    return JsonResponse({'data': dat})


def normalize(request):
    data = json.loads(request.body)
    text = data.get('text')
    return HttpResponse(text.lower())

