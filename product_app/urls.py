from django.contrib import admin
from django.urls import path
from product_app import views
from .views import (product_detail_view,product_create_detail_view,product_detail_delete,show_product_page,product_update_view,registration,user_login)
from django.conf.urls import url
# 
urlpatterns = [


    path('/',views.product_create_detail_view),
    # path('showproductpage/',views.show_product_page),
    path('<int:my_id>/',views.product_detail_view,name='product-detail'),
    path('',views.show_product_page,name='product-list'), #homepage
    path('<int:my_id>/delete',views.product_detail_delete,name='product-delete'),
    path('<int:id>/update',views.product_update_view,name='product-update'),
    # path('<int:id>/cart',views.cart,name='product-cart'),
    # path('<int:id>/checkout',views.checkout,name='product-checkout'),
   
    

    

]