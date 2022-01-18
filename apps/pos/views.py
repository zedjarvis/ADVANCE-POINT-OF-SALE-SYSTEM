from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Avg, Sum, Max, Min, FloatField, Count, Q
# Create your views here.
from .models import Item, Category


@login_required
@staff_member_required(login_url='login')
def dashboard(request):
    # request.session.set_expiry(60 * 15)

    try:
        # get total value of items in stock
        total_val = int(Item.objects.filter(quantity__gte=1).aggregate(
            total_value=Sum('value'))['total_value'])

        total_cost = int(Item.objects.filter(quantity__gte=1).aggregate(
            total_cost=Sum('purchase_value'))['total_cost'])

        # Total profit with commas and 2dp
        total_profit = "{0:,.2f}".format(total_val - total_cost)

        # 2dp and thousand separator
        total_val = "{0:,.2f}".format(total_val)
        total_cost = "{0:,.2f}".format(total_cost)
    except (Exception) as e:
        print(str(e))
        total_val = "{0:,.2f}".format(0)
        total_cost = "{0:,.2f}".format(0)
        total_profit = "{0:,.2f}".format(0)

    # get number of items in inventory
    number_of_items = Item.objects.all().count()

    # get number of items in stock
    items_in_stock = Item.objects.filter(quantity__gte=1).count()

    context = {'dashboard': 'active',
               'total_value': total_val,
               'total_cost': total_cost,
               'total_profit': total_profit,
               'number_of_items': number_of_items,
               'items_in_stock': items_in_stock,
               }
    return render(request, 'pos/dashboard.html', context)


@login_required
def view_items_inventory(request):
    items = Item.objects.all()
    categories = Category.objects.all()
    context = {'inventory': 'active',
               'items': items,
               'categories': categories}
    return render(request, 'pos/inventory2.html', context)


@login_required
def view_payments(request):
    context = {'payments': 'active'}
    return render(request, 'pos/payments.html', context)


@login_required
def point_of_sale(request):
    context = {'pos': 'active'}
    return render(request, 'pos/point_of_sale.html', context)
