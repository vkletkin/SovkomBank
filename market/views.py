from django.shortcuts import render
from .models import Product, Order
from django.db.models import Max, Min
import datetime


def task(request):

    start_date = datetime.date(2022, 6, 5)
    end_date = datetime.date(2022, 6, 10)

    Minproduct = Order.objects.filter(sale_date__range=(start_date, end_date)).order_by("quantity")[:1]
    Maxproduct = Order.objects.filter(sale_date__range=(start_date, end_date)).order_by("-quantity")[:1]

   # Book.objects.aggregate(price_diff=Max('price', output_field=FloatField()) - Avg('price'))
    #tas1maxPopular = Order.objects.filter(pub_date__range=(start_date, end_date)).values('sale_date').annotate(min_price=Min("price")).order_by()

    return render(request, "task.html", {"Minproduct": Minproduct[0].name,"Maxproduct": Maxproduct[0].name  })


def show_orders(request):
    orders = Order.objects.all()[:10]

    return render(request, "show_orders.html", {"orders": orders})


def show_products(request):
    products = Product.objects.all()[:10]

    return render(request, "show_products.html", {"products": products})
