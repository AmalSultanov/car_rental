from django.urls import path

from api.views import CarListAPIView, CarRetrieveAPIView

app_name = 'api'

urlpatterns = [
    path('cars/', CarListAPIView.as_view()),
    path('cars/<int:pk>/', CarRetrieveAPIView.as_view())
]
