from django.forms import forms
from .models import Transaction, PaymentMethod

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        exclude = ['status']



class PaymentMethodForm(forms.ModelForm):
    class Meta:
        model = PaymentMethod
        exclude = ["transaction"]