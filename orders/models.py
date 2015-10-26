from django.db import models


class Order(models.Model):
    marketplace = models.CharField(max_length=50)
    order_id = models.CharField(max_length=50)
    order_purchase_date = models.CharField(max_length=15, blank=True)
    order_purchase_heure = models.CharField(max_length=15, blank=True)
    order_amount = models.CharField(max_length=50)
