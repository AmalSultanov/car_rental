from django.contrib import admin
from django.db import ProgrammingError
from modeltranslation.admin import TranslationAdmin

from offers.models import (ServicesImageModel, CarsImageModel, CarModel,
                           BrandModel, TypeModel, PowerModel, FuelModel,
                           DriveModel, TransmissionModel, ColorModel,
                           YearModel, CarImageModel)


class MyTranslationAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(ServicesImageModel)
class ServicesImageModelAdmin(MyTranslationAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['title', 'created_at']
    search_fields = ['title']

    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        try:
            ServicesImageModel.load().save()
        except ProgrammingError:
            pass

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(CarsImageModel)
class CarsImageModelAdmin(MyTranslationAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['title', 'created_at']
    search_fields = ['title']

    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        try:
            CarsImageModel.load().save()
        except ProgrammingError:
            pass

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(BrandModel)
class BrandModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['title', 'created_at']
    search_fields = ['title']


@admin.register(TypeModel)
class TypeModelAdmin(MyTranslationAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['title', 'created_at']
    search_fields = ['title']


@admin.register(PowerModel)
class PowerModelAdmin(admin.ModelAdmin):
    list_display = ['amount', 'created_at']
    list_filter = ['amount', 'created_at']
    search_fields = ['amount']


@admin.register(FuelModel)
class FuelModelAdmin(MyTranslationAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['title', 'created_at']
    search_fields = ['title']


@admin.register(DriveModel)
class DriveModelAdmin(MyTranslationAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['title', 'created_at']
    search_fields = ['title']


@admin.register(TransmissionModel)
class TransmissionModelAdmin(MyTranslationAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['title', 'created_at']
    search_fields = ['title']


@admin.register(ColorModel)
class ColorModelAdmin(MyTranslationAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['title', 'created_at']
    search_fields = ['title']


@admin.register(YearModel)
class YearModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['title', 'created_at']
    search_fields = ['title']


class CarImageModelAdmin(admin.TabularInline):
    model = CarImageModel


@admin.register(CarModel)
class CarModelAdmin(MyTranslationAdmin):
    list_display = ['title', 'price', 'type',
                    'drive', 'year', 'created_at']
    list_filter = ['brand', 'price', 'type', 'power', 'fuel',
                   'drive', 'year', 'color', 'created_at']
    search_fields = ['title', 'brand', 'type', 'type', 'power',
                     'fuel', 'drive', 'year', 'transmission', 'color']
    autocomplete_fields = ['brand', 'type', 'power', 'fuel',
                           'drive', 'transmission', 'color', 'year']

    inlines = [CarImageModelAdmin]
