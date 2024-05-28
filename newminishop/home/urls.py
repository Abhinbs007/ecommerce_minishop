
from django.urls import path
from . import views


urlpatterns  =[
    path('',views.home,name='index'),
    path('about',views.about,name='about'),
    path('<slug:c_slug>/',views.home,name='pro_cat'),
    path('<slug:c_slug>/<slug:product_slug>',views.details,name='product_slug'),
    path('search',views.search,name='search')



]