from django import forms
from .models import product
from django.contrib.auth.models import User
from product_app.models import UserProfileInfo
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model= User
        fields = ('username','email','password')
class UserProfileInforForm(forms.ModelForm):
    class Meta():
        model= UserProfileInfo
        fields = ('portfolio_site','userProfile')

class ProductForm(forms.ModelForm):
    title       =   forms.CharField(
                          required=True,
                          widget=forms.TextInput(
                              attrs={"placeholder":"Your Title"}
                          ))
    email= forms.EmailField()
    description =   forms.CharField(
                          required=False,
                          widget=forms.Textarea(
                                 attrs={
                                     "placeholder":"Ypur descriptiopn",
                                     "class":"new-class-name two",
                                     "id":"my-id-for-textarea",
                                     "rows":20,
                                     "cols":100

                                     }
                                )
                            )
    price       =   forms.DecimalField(initial=199.99)
    sumary      =   forms.CharField(initial='Hello')
    featured    =   forms.BooleanField()
    class Meta:
        model=product
        fields=[
            'title',
            'description',
            'price',
            'sumary',
            'featured'
        ]
def clean_title(self,*args,**kwargs ):
    title= self.cleaned_data.get("title")
    if not "CFE" in title:
        raise forms.ValidationError("This is not a valid title")
    if not "news" in title:
        raise forms.ValidationError("This is not a valid title")
    return title
    
def clean_email(self,*args,**kwargs):
    email=self.cleaned_data.get("email")
    if not "edu" in email:
        raise forms.ValidationError("this is not valid email")     
class RawProductForm(forms.Form):
    title       =   forms.CharField(
                          required=True,
                          widget=forms.TextInput(
                              attrs={"placeholder":"Your Title"}
                          ))
    description =   forms.CharField(
                          required=False,
                          widget=forms.Textarea(
                                 attrs={
                                     "placeholder":"Ypur descriptiopn",
                                     "class":"new-class-name two",
                                     "id":"my-id-for-textarea",
                                     "rows":20,
                                     "cols":100

                                     }
                                )
                            )
    price       =   forms.DecimalField(initial=199.99)
    sumary      =   forms.CharField(initial='Hello')
    featured    =   forms.BooleanField()
class RawBookingForm(forms.Form):
    emailBooking =forms.CharField()
    numberOfAdult=forms.ChoiceField(required=True)
    nunverOfChild=forms.ChoiceField()
    requestInfor=forms.Textarea()