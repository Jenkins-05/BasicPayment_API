from django.urls import path
from .views import make_payments

urlpatterns = [
    path("", make_payments),
]   