from django.urls import path
from . import views


urlpatterns = [
    # [ GET ]
    path('products/', views.all_products, name= 'products'),
    path('products/<str:name>/', views.product_by_name, name ='product'),
    
    # [ GET ]
    path('category/<str:title>/', views.products_by_category, name= 'category'),
    
    # [ GET ]
    path('cart/', views.get_cart_items, name= 'cart'),
    
    # [ POST | DELETE ]
    path('cart_item/<int:id>/', views.cart_operations.as_view(), name= 'cart_item'),
    
    # [ PUT ]
    path('cart_item/<int:id>/<str:operation>/', views.edit_cart_item, name= 'cart_item_edit'),
]
