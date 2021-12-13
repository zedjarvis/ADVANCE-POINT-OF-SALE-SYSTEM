# -*- encoding: utf-8 -*-
"""
__author__ = Cedrouseroll Omondi
__email__ = omondicedo@gmail.com
"""

from django.urls import path
from .views import inventory, pos

urlpatterns = [
    # create edit delete category restful api
    path('create_category/',
         inventory.CreateCategory.as_view(), name="create_category"),

    # create edit delete item restul api
    path('create_item/',
         inventory.CreateItem.as_view(), name='create_item'),
    path('delete_item/', inventory.deleteItem, name='delete_item'),
    path('edit_item/<int:id>/',
         inventory.EditItem.as_view(), name='edit_item'),

    # point of sale page
    path('get_item_price/', pos.get_item_price),
    path('get_object_list/', pos.get_list_forautocomplete),
    path('update_purchased_items', pos.get_purchased_items),
]
