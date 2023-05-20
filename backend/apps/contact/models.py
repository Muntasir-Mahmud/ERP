from django.db import models


class Contact(models.Model):
    """
    Model class for Contacts
    """
    name = models.CharField(max_length=255, null=True)
    phone = models.IntegerField(unique=False, blank=False)
    address = models.TextField(unique=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.name


class Customer(models.Model):
    """
    Model class for Customers
    """
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE)


class Supplier(models.Model):
    """
    Model class for Customers
    """
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE)
