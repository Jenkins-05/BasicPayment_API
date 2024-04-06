from django.shortcuts import render
from .serializers import TransactionSerializer, PaymentSerializer
from rest_framework.viewsets import ModelViewSet
from users.models import User
from .models import Transaction

class TransactionViewset(ModelViewSet):
    
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
