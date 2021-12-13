from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.
from .models import Item, Category


@login_required
@staff_member_required(login_url='login')
def dashboard(request):
    request.session.set_expiry(60 * 15)
    context = {'dashboard': 'active'}
    return render(request, 'pos/dashboard.html', context)


@login_required
def view_items_inventory(request):
    items = Item.objects.all()
    categories = Category.objects.all()
    context = {'inventory': 'active',
               'items': items,
               'categories': categories}
    return render(request, 'pos/inventory.html', context)


@login_required
def view_payments(request):
    context = {'payments': 'active'}
    return render(request, 'pos/payments.html', context)


@login_required
def point_of_sale(request):
    context = {'pos': 'active'}
    return render(request, 'pos/point_of_sale.html', context)
