from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, APIView
from .models import *

# Create your views here.


@api_view(['GET'])
def all_products(request):
    return JsonResponse({'all_products':list(Product.objects.all().values())})

@api_view(['GET'])
def product_by_name(request, name):
    product = Product.objects.filter(name = name).values().first()
    return JsonResponse({'product': product})
    
@api_view(['GET'])
def products_by_category(request, title):
    category = Category.objects.all().get(title = title)
    products = list(Product.objects.all().filter( category = category).values())
    return JsonResponse({f"{category.title}": products})

@api_view(['GET'])
def get_cart_items(request):
        cart_items = list(CartItem.objects.all().values())
        products =[dict(Product.objects.all().filter(id = product['product_id']).values().first())for product in cart_items]
        total_price = 0
        for product in range(len(products)):
            category_id = products[product]['category_id']
            products[product]['category'] = Category.objects.all().get(id = category_id).title
            products[product]['quantity'] = cart_items[product]['quantity']
            total_price += products[product]['price'] * products[product]['quantity']
        return JsonResponse({'cart_items' : products, 'cart_total': total_price})


@api_view(['PUT'])
def edit_cart_item(request, id, operation):
    cart_item = CartItem.objects.all().get( product = Product.objects.get(id = id))
    acceptable_operations = ['add', 'drop']
    if operation in acceptable_operations and operation == 'add':
        cart_item.quantity += 1
    elif operation in acceptable_operations and operation == 'drop':
        cart_item.quantity -=1
    cart_item.save()
    return JsonResponse({f"{cart_item.product.name}": f"{cart_item.quantity}"})
    
    
class cart_operations(APIView):
    
    
    def post(self, request, id):
        product = Product.objects.all().get( id = id)
        new_cart_item = CartItem.objects.get_or_create( product = product )
        new_cart_item[0].save()
        if new_cart_item[1]:
            return JsonResponse({'success':f"{product.name} has been added to your cart"})
        else:
            return JsonResponse({'Failure': "Item either does not exist or is already in your cart"})
    

        
    def delete(self, request, id):
        cart_item = CartItem.objects.all().get( product = Product.objects.get(id = id))
        name = cart_item.product.name
        cart_item.delete()
        return JsonResponse({"success": f"{name} has been deleted"})
            
    