from django.shortcuts import render
from .serializers import TransactionSerializer, PaymentSerializer


# Create your views here.
def make_payments(request):
    transaction_form = TransactionSerializer
    payment_method_form = PaymentSerializer

    if request.method == "GET":
        transaction = TransactionSerializer(request.DATA)
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

