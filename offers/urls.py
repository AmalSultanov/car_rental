from django.urls import path

from offers.views import CarsListView, CarsDetailView

app_name = 'offers'

urlpatterns = [
    path('<int:pk>/', CarsDetailView.as_view(), name='car-detail'),
    path('', CarsListView.as_view(), name='cars'),
]
