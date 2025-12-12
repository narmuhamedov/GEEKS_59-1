from django.urls import path
from products.views import all_products, meals_products, drinks_products


urlpatterns = [
    path('all_prod/', all_products, name='all_products'),
    path('meal_prod/', meals_products, name='meals_products'),
    path('drinks_prod/', drinks_products, name='drinks_products'),
]