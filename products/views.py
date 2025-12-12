from django.shortcuts import render
from products.models import Products
from django.core.paginator import Paginator


#all products
def all_products(request):
    if request.method == 'GET':
        products = Products.objects.all().order_by("-id")
        paginator = Paginator(products, 2)
        page = request.GET.get("page")
        page_obj = paginator.get_page(page)


        return render(
            request,
            'products/all_products.html',
            {
                'prod': page_obj
            }
        )

# meals
def meals_products(request):
    if request.method == 'GET':
        products = Products.objects.filter(categories__name='Еда').order_by("-id")
        return render(
            request,
            'products/meals_products.html',
            {
                'prod': products
            }
        )
    
# drinks
def drinks_products(request):
    if request.method == 'GET':
        products = Products.objects.filter(categories__name='Напитки').order_by("-id")
        return render(
            request,
            'products/drinks_products.html',
            {
                'prod': products
            }
        )