from django.shortcuts import render


# Create your views here.
from orders.models import SalesOrder


def orders_page(request):
    return render(request, 'index.html', {'orders': SalesOrder.objects.all()})
