from django.db import models


class ProductMapping(models.Model):
    product_id = models.IntegerField()
    brand = models.CharField(max_length=255)
    delivery_method = models.CharField(max_length=255)
