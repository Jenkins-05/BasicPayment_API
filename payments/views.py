from django.shortcuts import render
from .forms import TransactionForm, PaymentMethodForm

# Create your views here.
def make_payments(request):
    transaction_form = TransactionForm()
    payment_method_form = PaymentMethodForm()

    if request.method == "GET":
        transaction_form(request)
        payment_method_form(request)

        if transaction_form.is_valid() and payment_method_form.is_valid():
            transaction_form.save()


    return render(

        request,
        {
            'transaction_form': transaction_form,
            'payment_form': payment_method_form
        }
    )
