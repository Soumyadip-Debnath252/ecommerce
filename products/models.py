from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL
# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=100 ,unique=True)
    slug=models.SlugField(unique=True)
    featured=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title']
    
    def __str__(self):
        return self.title
    
class Product(models.Model):
    title=models.CharField(max_length=100,unique=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products')
    slug=models.SlugField(unique=True)
    featured=models.BooleanField(default=False)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    thambnali=models.URLField()
    is_stock=models.BooleanField(default=True)
    description=models.TextField(blank=True,null=True,default='N/A')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']
    def __str__(self):
        return self.title
    

class Slider(models.Model):
    title=models.CharField(max_length=100)
    banner=models.ImageField(upload_to='banners')
    show=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    
class cart(models.Model):
    product_name=models.ForeignKey(Product,related_name='product_names',on_delete=models.CASCADE)
    slug=models.SlugField(unique=True)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    thambnali=models.URLField()
    quantity=models.IntegerField(default=1)