from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import TransactionViewset

router = SimpleRouter()
router.register(r'', TransactionViewset)

urlpatterns = router.urls