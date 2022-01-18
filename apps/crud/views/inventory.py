# -*- encoding: utf-8 -*-
"""
__author__ = Cedrouseroll Omondi
__email__ = omondicedo@gmail.com
"""

from django.shortcuts import redirect
from django.views.generic.base import View
from apps.pos.models import Item, Category
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt


class CreateCategory(View):
    def post(self, request):
        try:
            category_name = request.POST.get('category_name')
            category = Category(category_name=category_name)
            category.save()
            return JsonResponse({'category_name': category.category_name})
        except (Exception) as e:
            return JsonResponse({'error': str(e)})


class CreateItem(View):
    def post(self, request):
        item_name = request.POST.get('item_name', None)
        item_description = request.POST.get('description', None)
        item_quantity = request.POST.get('quantity', None)
        unit_price = request.POST.get('item_price', None)
        purchase_price = request.POST.get('purchase_price', None)
        reorder_level = request.POST.get('reorder_level')
        reoder_quantity = request.POST.get('reorder_quantity', None)
        location = request.POST.get('location', None)
        category_name = request.POST.get('category', None)

        # get category
        category = Category.objects.get(category_name=category_name)

        item = Item(item_name=item_name, description=item_description,
                    quantity=item_quantity, unit_price=unit_price,
                    purchase_price=purchase_price,
                    reorder_level=reorder_level,
                    reorder_quantity=reoder_quantity,
                    location=location, category=category)
        item.save()

        data = {'id': item.id,
                'item_name': item.item_name,
                'description': item.description,
                'quantity': item.quantity,
                'unit_price': item.unit_price,
                'value': item.value,
                'purchase_price': item.purchase_price,
                'reorder_level': item.reorder_level,
                'reorder_quantity': item.reorder_quantity,
                'location': item.location,
                'category': item.category.category_name,
                }

        return JsonResponse({'item': data})


# Edit item class
class EditItem(View):
    def post(self, request, id):
        item_name = request.POST.get('item_name')
        item_description = request.POST.get('description')
        item_quantity = request.POST.get('quantity')
        unit_price = request.POST.get('item_price')
        purchase_price = request.POST.get('purchase_price')
        reorder_level = request.POST.get('reorder_level')
        reorder_quantity = request.POST.get('reorder_quantity')
        location = request.POST.get('location')
        category_name = request.POST.get('category')

        # get category
        category = Category.objects.get(category_name=category_name)

        item = Item.objects.get(id=id)
        item.item_name = item_name
        item.description = item_description
        item.quantity = item_quantity
        item.unit_price = unit_price
        item.purchase_price = purchase_price
        item.reorder_level = reorder_level
        item.reorder_quantity = reorder_quantity
        item.location = location
        item.cateogry = category
        item.save()

        return redirect('inventory')


@csrf_exempt
def deleteItem(request):
    # delete item or return an error message
    if request.method == 'GET':
        try:
            item_id = request.GET.get('item_id', None)
            item = Item.objects.get(id=item_id)
            name = item.item_name
            item.delete()
            return JsonResponse({'item': name})
        except (Exception) as e:
            return JsonResponse({'error': str(e)})

    else:
        return JsonResponse({'invalid': 'invalid request'})
