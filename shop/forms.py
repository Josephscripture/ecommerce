from django.forms import ModelForm
from .models import Products,User,Category
from django.contrib.auth.forms import UserCreationForm



class ProductForm(ModelForm):
    class Meta:
        model=Products
        fields= '__all__'




class signupForm(UserCreationForm):
    class Meta:
        model=User
        fields='__all__'

class CategoryForm(ModelForm):
    class Meta:
        model=Category
        fields=['name']



class CartForm(ModelForm):
    class Meta:
        model=Products
        fields='__all__'


        