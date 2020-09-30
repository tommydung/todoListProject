from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import os
# from product_app.models import product

# Create your models here.
# def default_place_pics():
#     return "/media/static/images/social1.png"

class UserProfileInfo(models.Model):
    user =models.OneToOneField(User,on_delete=models.CASCADE)
    #additional
    userProfile =models.ImageField(upload_to='profile_pic',blank=True)
    portfolio_site=models.URLField(blank=True)
    portfolio_pic=models.ImageField(upload_to='profile_pic',blank=True)
    def __str__(self):
        return self.user.username
    
class product(models.Model):
    title       = models.CharField(max_length=128)
    description  = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2,max_digits=1000)
    sumary      = models.TextField()
    featured    = models.BooleanField()
    image       =models.ImageField(upload_to='static/images',default = 'media/static/images/dogs.png')
    def get_absolute_url(self):
        # return f"/product/{self.id}" 
        return reverse("product-detail",kwargs={"my_id":self.id})
    def get_absolute_url_delete(self):
        return reverse("product-delete",kwargs={"my_id":self.id})   
    def get_absolute_url_update(self):
        return reverse("product-update",kwargs={"id":self.id})
    # def get_absolute_url_cart(self):
    #     return reverse("product-cart",kwargs={"my_id":self.id})
    # def get_absolute_url_checkout(self):
    #     return reverse("product-checkout")
    # def showImage(self):
    #     new_product = product.objects.get(id=my_id)
    #     return reverse("",kwargs={"static/images":self.image})
