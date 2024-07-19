from django.contrib import admin
from django.db import ProgrammingError
from modeltranslation.admin import TranslationAdmin

from pages.models import (ContactModel, ContactInfoModel, ContactImageModel,
                          HomeImageModel)


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


@admin.register(HomeImageModel)
class HomeImageModelAdmin(MyTranslationAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['title', 'created_at']
    search_fields = ['title']

    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        try:
            HomeImageModel.load().save()
        except ProgrammingError:
            pass

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(ContactImageModel)
class ContactImageModelAdmin(MyTranslationAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['title', 'created_at']
    search_fields = ['title']

    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        try:
            ContactImageModel.load().save()
        except ProgrammingError:
            pass

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'created_at']
    list_filter = ['created_at']
    search_fields = ['first_name', 'last_name', 'email', 'message']


@admin.register(ContactInfoModel)
class ContactInfoModelAdmin(MyTranslationAdmin):
    list_display = ['address', 'phone', 'email', 'created_at']
    list_filter = ['address', 'phone', 'created_at']
    search_fields = ['address', 'phone', 'email']

    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        try:
            ContactInfoModel.load().save()
        except ProgrammingError:
            pass

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
