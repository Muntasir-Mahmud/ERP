from django.db import models

from contact.models import Customer, Supplier


class CustomerDebit(models.Model):
    """
    Model class for Product
    """
    customer = models.ForeignKey(Customer, null=False,
                                 on_delete=models.CASCADE)
    amount = models.IntegerField(null=False)
    created_on = models.DateTimeField(auto_now_add=True)


class SupplierCredit(models.Model):
    """
    Model class for Product
    """
    supplier = models.ForeignKey(Supplier, null=False, on_delete=models.CASCADE)
    amount = models.IntegerField(null=False)
    created_on = models.DateTimeField(auto_now_add=True)
