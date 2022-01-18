# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021 - Cedrouseroll
"""

from django.urls import path
from .views import dashboard, view_items_inventory, view_payments, point_of_sale

urlpatterns = [
    path('dashboard/', dashboard, name="dashboard"),
    path('inventory/', view_items_inventory, name="inventory"),
    path('payments/', view_payments, name="payments"),
    path('process_sales/', point_of_sale, name="pos"),
]
