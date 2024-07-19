from modeltranslation.translator import register, TranslationOptions

from pages.models import HomeImageModel, ContactImageModel, ContactInfoModel


@register(HomeImageModel)
class HomeImageTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(ContactImageModel)
class ContactImageTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(ContactInfoModel)
class ContactInfoTranslationOptions(TranslationOptions):
    fields = ('address',)
