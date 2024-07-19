from django.contrib import admin
from django.db import ProgrammingError
from modeltranslation.admin import TranslationAdmin

from info.models import (AboutImageModel, InfoModel, TeamModel,
                         HistoryModel, BlogImageModel, PostModel,
                         PostTagModel, CategoryModel, CommentModel)


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


@admin.register(AboutImageModel)
class AboutImageModelAdmin(MyTranslationAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['title', 'created_at']
    search_fields = ['title']

    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        try:
            AboutImageModel.load().save()
        except ProgrammingError:
            pass

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(InfoModel)
class InfoModelAdmin(MyTranslationAdmin):
    list_display = ['title', 'description', 'created_at']
    list_filter = ['title', 'created_at']
    search_fields = ['title', 'description']

    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        try:
            InfoModel.load().save()
        except ProgrammingError:
            pass

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(TeamModel)
class TeamModelAdmin(MyTranslationAdmin):
    list_display = ['name', 'position', 'description', 'created_at']
    list_filter = ['name', 'position', 'created_at']
    search_fields = ['position', 'name', 'description']


@admin.register(HistoryModel)
class HistoryModelAdmin(MyTranslationAdmin):
    list_display = ['title', 'description', 'created_at']
    list_filter = ['title', 'created_at']
    search_fields = ['title', 'description']

    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        try:
            HistoryModel.load().save()
        except ProgrammingError:
            pass

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(BlogImageModel)
class BlogImageModelAdmin(MyTranslationAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['title', 'created_at']
    search_fields = ['title']

    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)
        try:
            BlogImageModel.load().save()
        except ProgrammingError:
            pass

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(PostModel)
class PostModelAdmin(MyTranslationAdmin):
    list_display = ['title', 'category', 'created_at']
    list_filter = ['title', 'category', 'tags', 'created_at']
    search_fields = ['title', 'category', 'tags']
    autocomplete_fields = ['category', 'tags']


@admin.register(PostTagModel)
class PostTagModelAdmin(MyTranslationAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(CategoryModel)
class CategoryModelAdmin(MyTranslationAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(CommentModel)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name']
