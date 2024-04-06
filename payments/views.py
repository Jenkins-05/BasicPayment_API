from django.shortcuts import render
from .serializers import TransactionSerializer, PaymentSerializer
from rest_framework.viewsets import ModelViewSet
from users.models import User
from .models import Transaction

class TransactionViewset(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(user=self.request.user.id)
        return query_set