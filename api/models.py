from django.db import models

# Create your models here.
class Dresses(models.Model):
    category = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=400)
    rating = models.IntegerField()
    discount = models.IntegerField(default=0)
    price = models.IntegerField()
    sold = models.BooleanField(default=False)
    delivery = models.CharField(default="free delivery", max_length=50)
    image = models.ImageField(upload_to='image/')# Specify the upload directory
  
  
    def __str__(self):
        return self.name

class AddtoCart(models.Model):
    product_id = models.IntegerField()
    quantity = models.IntegerField(default=1)
    size = models.CharField(max_length=20)
    rating = models.IntegerField(default=0)
    review = models.TextField(blank=True, null=True, default="good")
    preference = models.CharField(max_length=30, default="")

    def __str__(self):
        return f'Product ID: {self.product_id}, Quantity: {self.quantity}, Size: {self.size}, Rating: {self.rating}, Reviews: [{self.review}]'
    
class Order(models.Model):
    product_id = models.IntegerField()
    quantity = models.IntegerField(default=1)
      # Assuming you have user authentication

    def __str__(self):
        return f'Order {self.id} - Product ID: {self.product_id}, Quantity: {self.quantity}'
