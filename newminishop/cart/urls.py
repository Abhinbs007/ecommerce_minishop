from django.urls import path
from . import views



urlpatterns  =[

  path('cartDetails',views.cart_details,name='cartDetails'),
  path('add/<int:product_id>/',views.add_cart,name='addcart'),
  path('checkout',views.checkout,name='checkout'),
  path('minus_cart/<int:product_id>/',views.min_cart,name='minus_cart'),
  path('delete/<int:product_id>/',views.min_cart,name='delete_from_cart'),
  ]
