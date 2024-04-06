from django.contrib import admin
from .models import Transaction, PaymentMethod

# Register your models here.
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ["user", "amount", "status", "created" ]
    list_filter = [ "user", "status", "created"]