from unicodedata import name
from django.http import HttpResponse, JsonResponse
import json

from .models import category

def list(request):
    cate = category.objects.values()

    data = []
    for value in cate:
        data.append(value)
    return JsonResponse({'status': True, 'message': '', 'data': data})

def create(request):
    body = request.body
    body = body.decode()
    body = json.loads(body)
    cate = category(name = body['name'])
    cate.save()
    return HttpResponse('Create category.')
