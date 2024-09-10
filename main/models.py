from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DateField(auto_now_add=True)
    description = models.TextField()
    genre = models.CharField(max_length=255)


