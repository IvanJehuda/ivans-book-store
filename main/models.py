from django.db import models
import uuid


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # tambahkan baris ini
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    genre = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='-')


