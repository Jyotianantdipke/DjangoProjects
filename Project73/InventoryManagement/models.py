from django.db import models

# Create your models here.
class Product(models.Model):
    Date=models.DateField()
    Provider=models.CharField(max_length=32)
    Name_of_Product=models.CharField(max_length=32)
    Price=models.IntegerField()
    Quantity=models.IntegerField()
    Amount=models.IntegerField()
    Stock=models.IntegerField()