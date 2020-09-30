"""product_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url,include
from product_app import views
from product_app.views import (contact_view,cart,checkout,registration,user_login,cart,checkout)
from django.conf.urls.static import static # new
from django.conf import settings # new
# app_name ='product_app'
urlpatterns = [
    path('products/',include('product_app.urls')),
    path('admin/', admin.site.urls),
   
    # path('',views.home_view.as_view(),name='home'),
    path('success.html/',views.Success.as_view(),name='success'),
    path('faq/',views.faq_view,name='faq'),
    path('about/',views.about_view,name='about'),
    path('social/',views.social_view,name='socail'),
    path('contact/',views.contact_view,name='contact'),
    path('registration/',views.registration,name='registration'),
    path('user_login/',views.user_login,name='login'),
    url(r'^$',views.index,name='index'),
    url(r'^logout/',views.user_logout,name='logout'),
    url(r'special/',views.special,name='special'),
    url(r'^user_login/',views.user_login,name='user_login'),
    url(r'^registration/',views.registration,name='register'),

    
    # path('login/login.html',views.user_login.as_,name='login'),
    # url(r'^logout/$',views.user_logout.name='logout'),
    # url(r'special/',views.special,name='special'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    # path('')
   
  
]
if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)