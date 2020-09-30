from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import product,UserProfileInfo
from .forms import ProductForm,RawProductForm,RawBookingForm,UserForm,UserProfileInforForm
from django.conf import settings
from django.views.generic.base import TemplateView
# from django.core.urlresolvers import reverse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

# Create your views here.
# def home_view(request,*args, **kwargs):
#     print(request.user)
#     print(product_app.url)
#     return render(request,"index.html",{})

# payments/views.py
def index(request):
    return render(request,'index.html')
    print(request)


# class HomePageView(TemplateView):
#     template_name = 'index.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['key'] = settings.RAVE_PUBLIC_KEY
#         return context
#     # print(args,kwargs)
#     print(request.user)
#     print(url)
    # # return HttpResponse("<h1>Hello World</h1>") #string html code
    # return render(request,"index.html",{})
class Success(TemplateView):
    template_name = 'success.html'

@login_required
def special(request):
    return HttpResponse("You are login,Nice")
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
def registration(request,*args, **kwargs):
    registered= False
    if request.method=="POST":
        user_form= UserForm(data=request.POST)
        profile_form=UserProfileInforForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user= user_form.save()
            user.set_password(user.password)
            user.save()
            profile =profile_form.save(commit=False)
            profile.user=user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
                profile.save()
            registered=True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=UserProfileInforForm()
    return render(request,'registration.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})
def user_login(request):
    
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:# this is not a function
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('ACCOUNT NOT ACTIVE')
        else:
            print("Some one tried to login in and failed")
            print("Username: {} and password {}" .format(username,password))
            return HttpResponse("invalid login details supplied")
    else:
        return render(request,'login.html',{})
def contact_view(request,*args, **kwargs):
    return render(request,'contact.html',{}) #string html code
def faq_view(request,*args, **kwargs):
    return render(request,'faq.html',{}) #string html code
def social_view(request,*args, **kwargs):
    return render(request,'social.html',{}) #string html code

def about_view(request,*args, **kwargs):
    my_context={
        "my_text":"this is about django",
        "my_number": 3466668010,
        "my_list":[123,123,123,1234],
    }
    return render(request,'about.html',my_context) #string html code
def cart(request):
    context={}
    return render(request,'cart.html',context)
def checkout(request):
    context={}
    return render(request,'checkout.html',context)
def product_detail_view(request,my_id):
    #3 way to check product not show
    obj= product.objects.get(id=my_id)
    obj=get_object_or_404(product,id=my_id)


    # try:
    #     obj= product.objects.get(id=my_id)
    # except product.DoesNotExist:
    #     pass
    # if request.method=="POST":
        
    context={
        # 'title':obj.title,
        # 'description':obj.description,
        # 'price':obj.price,
        # 'sumary':obj.sumary,
        # 'featured':obj.featured,
        'o':obj

    }
    return render(request,"products/product_detail.html",context)
def cart(request,*args, **kwargs):
    # obj_cart= product.objects.get(id=my_id)
    # obj_cart=get_object_or_404(product,id=my_id)
    context={
        # 'oc':obj_cart
    }
    return render(request,'products/cart.html',context) #string html code
def checkout(request,*args, **kwargs):
    # obj_checkout= product.objects.get(id=my_id)
    # obj_checkout=get_object_or_404(product,id=my_id)
    context={
        # 'ocheck':obj_checkout
    }
    return render(request,'products/checkout.html',context) #string html code
def product_update_view(request,id=id):
    obj=get_object_or_404(product,id=id)
    form = ProductForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
    context ={
        'form':form
    }
    return render(request,"products/product_create.html",context)
def product_detail_delete(request,my_id):
    obj= product.objects.get(id=my_id)
    if request.method=="POST":
        obj.delete()
        return redirect('../../')
        print(obj[my_id])
        print(obj.image)
        # print(obj.image.u)
    context={
        # 'title':obj.title,
        # 'description':obj.description,
        # 'price':obj.price,
        # 'sumary':obj.sumary,
        # 'featured':obj.featured,
        'o':obj

    }
    return render(request,"products/product_delete.html",context)
def product_create_detail_view(request):
    # form= ProductForm(request.POST or None)
    # if form.is_valid():
    #     form.save()
    #     form= ProductForm()
    # context_form={
    #     # 'title':obj.title,
    #     # 'description':obj.description,
    #     # 'price':obj.price,
    #     # 'sumary':obj.sumary,
    #     # 'featured':obj.featured,
    #     'form':form
    #}
    my_form=RawProductForm()
    if request.method=="POST":
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            product.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)
    context={
            "form":my_form
    }
        # print(request.GET)
        # print(request.POST)
        # my_new_title=request.POST.get('title')
        # print(my_new_title)
    #product.objects.create(title=my_new_title)
    # context={}
    # }
    return render(request,"products/product_create.html",context)
def show_product_page(request):
    # queryset= product.objects.all()
    all_product= product.objects.all()
    # all_product.save()
    context_all_product={
        "op_list":all_product
    }
    
    return render(request,"products/product_page.html",context_all_product)
def booking_information(request):
    if request.method=="POST":
        booking_form= RawBookingForm(request.POST)
        if booking_form.is_valid():
            print(booking_form.cleaned_data)
        else:
            print(booking_form.errors)
    context={"form":booking_form}
    return render(request,"products/booking.html",context)
