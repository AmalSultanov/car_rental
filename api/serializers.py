from rest_framework import serializers

from offers.models import (CarModel, BrandModel, TypeModel, PowerModel,
                           FuelModel, DriveModel, ColorModel, YearModel)


class BrandModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandModel
        fields = '__all__'


class TypeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeModel
        exclude = ['title_en', 'title_ru']


class PowerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PowerModel
        fields = '__all__'


class FuelModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelModel
        exclude = ['title_en', 'title_ru']


class DriveModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriveModel
        exclude = ['title_en', 'title_ru']


class TransmissionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriveModel
        exclude = ['title_en', 'title_ru']


class ColorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorModel
        exclude = ['title_en', 'title_ru']


class YearModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = YearModel
        fields = '__all__'


class CarModelSerializer(serializers.ModelSerializer):
    brand = BrandModelSerializer()
    type = TypeModelSerializer()
    power = PowerModelSerializer()
    fuel = FuelModelSerializer()
    drive = DriveModelSerializer()
    transmission = TransmissionModelSerializer()
    color = ColorModelSerializer()
    year = YearModelSerializer()

    class Meta:
        model = CarModel
        exclude = ['title_en', 'title_ru', 'description_en', 'description_ru']
