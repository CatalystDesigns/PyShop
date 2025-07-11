from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=64)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField('2083')


class Offer(models.Model):
    code = models.CharField(max_length=32)
    description = models.CharField(max_length=256)
    discount = models.FloatField()
