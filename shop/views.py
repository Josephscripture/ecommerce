from django.shortcuts import render,redirect
from .models import Products, Category
from django.http import HttpResponse
from .forms import ProductForm,signupForm,CategoryForm,CartForm
from django.contrib.auth import login,logout,authenticate
from django.db.models import Q



def home(request):
    q=request.GET.get('q', '')
    products=Products.objects.filter(Q(category__name__contains=q)|
    Q(name__contains=q))
    categories = Category.objects.all()
    context={'products':products, 'categories': categories}
    return render(request, 'shops/home.html', context)

#login view
def login_view(request):
    if request.method=='POST':
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
    
        
    return render(request,'shops/login.html')


#logout view
def logout_view(request):
    logout(request)
    return redirect('home')

#signup view
def signup_view(request):

    form=signupForm()
    context = {'form':form}
    if request.method=="POST":
        form=signupForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect ('login')
    return render(request,'shops/signup.html' , context)



def update_view(request):
    product=ProductForm()
    context={'product':product}
    if request.method =='POST':
        product=ProductForm(request.POST, request.FILES)
        if product.is_valid():
            product.save()
            return redirect('home')

    return render(request, 'shops/add.html', context)



def update_category(request):
    category=CategoryForm()
    context={'category':category}
    if request.method =="POST":
        category=CategoryForm(request.POST)
        if category.is_valid():
            category.save()
            return redirect('home')
    return render(request,'shops/category.html',context)


def delete_view(request,pk):
    category=Products.objects.get(pk=pk)
    if request.method=="POST":
        category.delete()
        return redirect('home')
    context={'category':category}
    return render(request,'shops/delete.html', context)



# def cart(request,pk):
#     category=CartForm()
#     # context={'category':category}
#     if request.method=='GET':
#         category=CartForm(request.GET)
#         category.save()
#         return redirect('home')
#     context={'category':category}
#     return redirect(request,'shops/cart.html' ,context)


    






    


