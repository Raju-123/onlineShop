from django.http import HttpResponse, JsonResponse
from .models import Product
from category.models import category

import json

# Create your views here.
def list(request):
    product = Product.objects.values()

    data = []
    for value in product:
        try:
            cate = category.objects.get(pk=value['category'])
        except Exception as e:
            return HttpResponse("No category exist")

        data.append(value)
    return JsonResponse({'status': True, 'message': '', 'data': data})


def create(request):
    validation = {}
    body = request.body
    body = body.decode()
    body = json.loads(body)

    if 'name' not in body:
        validation['name'] = 'Name required'
    
    if 'price' not in body:
        validation['price'] = 'Price required'
    
    if 'category' not in body:
        validation['category'] = 'Category required'

    if validation:
        return JsonResponse({ "status": False, "message": validation})

    try:
        cate = category.objects.get(pk=body['category'])
    except Exception as e:
        return HttpResponse("No category exist")

    product = Product(name = body['name'], price = body['price'], category=body['category'])
    product.save()
    return HttpResponse('Create category.')