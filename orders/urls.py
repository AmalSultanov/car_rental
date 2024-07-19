from django.urls import path

from orders.views import CheckoutCreateView

app_name = 'orders'

urlpatterns = [
    path('<int:pk>/', CheckoutCreateView.as_view(), name='checkout'),
]
