from django.contrib import admin
from .models import  product
from product_app.models import UserProfileInfo

# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(product)