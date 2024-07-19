from modeltranslation.translator import register, TranslationOptions

from offers.models import (ServicesImageModel, CarsImageModel, TypeModel,
                           FuelModel, DriveModel, TransmissionModel,
                           ColorModel, CarModel)


@register(ServicesImageModel)
class ServicesImageTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(CarsImageModel)
class CarsImageTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(TypeModel)
class TypeTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(FuelModel)
class FuelTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(DriveModel)
class DriveTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(TransmissionModel)
class TransmissionTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(ColorModel)
class ColorTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(CarModel)
class CarTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)
