from django.shortcuts import render
from .serializers import TransactionSerializer, PaymentSerializer
from rest_framework.response import Response


# Create your views here.
def make_payments(request):


    if request.method == "POST":
        transaction = TransactionSerializer(request.DATA)


    return 
