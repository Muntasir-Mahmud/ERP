from django.db import models


class Product(models.Model):
    """
    Model class for Product
    """
    name = models.CharField(max_length=255, null=True)
    size = models.CharField(max_length=255, unique=False, blank=False)
    price = models.IntegerField(unique=False, blank=False)
    gms = models.IntegerField(unique=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name


class Stock(models.Model):
    """
    Model class for Stock
    """
    product = models.ForeignKey(Product, null=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(unique=False, blank=False)
    previous_quantity = models.IntegerField(unique=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
