from django.db import models
from users.models import User


# Create your models here.
class Transaction(models.Model):
    STATUS_CHOICES = (
        ('SUCCEESS', 'success'),
        ('PENDING', 'pending'),
        ('DECLINED', 'declined'),
    )
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, related_name="transactions", on_delete=models.CASCADE)

    class Meta:
        ordering = ("-created", )


class PaymentMethod(models.Model):
    PAYMENT_METHOD = (
        ('MTN', 'MTN'),
        ('AIRTEL', 'AIRTEL')
    )
    
    name = models.CharField(max_length=255)
    description = models.TextField()

    transactions = models.OneToOneField(Transaction, related_name="payment_method", on_delete=models.CASCADE )

    