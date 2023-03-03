from django.db import models

# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length=20)
    id = models.UUIDField(primary_key=True, editable=False)
    credit = models.DecimalField(max_digits=15, decimal_places=2)
    def __str__(self):
        return self.username

class Invoice(models.Model):
    time_created = models.TimeField()
class Subscription(models.Model):
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    is_active = models.BooleanField(default=False)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    