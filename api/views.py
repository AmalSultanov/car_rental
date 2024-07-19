from rest_framework.generics import ListAPIView, RetrieveAPIView

from api.serializers import CarModelSerializer
from offers.models import CarModel


class CarListAPIView(ListAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer


class CarRetrieveAPIView(RetrieveAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer
