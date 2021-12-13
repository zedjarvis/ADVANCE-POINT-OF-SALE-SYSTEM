# -*- encoding: utf-8 -*-
"""
__author__ = Cedrouseroll Omondi
__email__ = omondicedo@gmail.com
"""

from apps.pos.models import Item, Category
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# my own modules
from apps.pos.utilities.utils import get_listof_values


# getting price info on sale process
@csrf_exempt
def get_item_price(request):
    # getting only the price of requested item
    if request.method == 'GET':
        try:
            item = Item.objects.get(
                item_name=request.GET.get('item'))
            return JsonResponse({'price': item.unit_price})
        except (Exception) as e:
            return JsonResponse({'error': "Please Check Item Name\n" + str(e)})
    else:
        return JsonResponse({'invalid': "Request Not a Get Request"})


# function to return a list of object name for autocompletion
@csrf_exempt
def get_list_forautocomplete(request):
    # the model to query from frontend
    if request.method == 'GET':
        try:
            model_to_query = request.GET.get('model')
            if model_to_query == 'category':
                name_to_get = "category_name"
                categories = Category.objects.values(name_to_get)
                category_list = get_listof_values(categories, name_to_get)
                return JsonResponse({'categories': category_list})
            else:
                name_to_get = "item_name"
                items = Item.objects.values(name_to_get)
                item_list = get_listof_values(items, name_to_get)
                return JsonResponse({'items': item_list})
        except (Exception) as e:
            return JsonResponse({'error': str(e)})
    else:
        return JsonResponse({'invalid': 'Request Not a Get Request'})


# get purchased item list and update sales and payments
@csrf_exempt
def get_purchased_items(request):
    if request.method == 'POST':
        try:
            purchased_items = request.POST.get('items')
            print(purchased_items)
            return JsonResponse({'msg': 'success'})
        except (Exception) as e:
            error = str(e)
            print(error)
            return JsonResponse({'error': error})
    else:
        return JsonResponse({'invalid': 'invalid request'})
