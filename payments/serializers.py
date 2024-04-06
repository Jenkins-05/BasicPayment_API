from rest_framework.serializers import ModelSerializer
from .models import PaymentMethod, Transaction

class PaymentSerializer(ModelSerializer):
    class Meta:
        model = PaymentMethod
        exclude = ["id"]


class TransactionSerializer(ModelSerializer):
    payment_method = PaymentSerializer()

    class Meta:
        model = Transaction
        exclude = ["id", "user", "status"]
