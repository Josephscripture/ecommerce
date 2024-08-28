from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50)


    def __str__(self):
        return self.name

class User(AbstractUser):
    name=models.CharField(max_length=100, null=True)
    email = models.EmailField(unique=True, null=True)
    first_name=models.CharField(max_length=100, null=True)
    last_name= models.CharField(max_length=100, null=True)
    image=models.ImageField(upload_to='images/', null=True)
    adress=models.CharField(max_length=100, null=True)
    username = models.CharField( max_length=200)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=[]
    
    






class Products(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()
    price=models.PositiveIntegerField()
    image=models.ImageField(upload_to='images/')
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    seller = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return (f"{self.name}|{self.description}|{self.category}")






