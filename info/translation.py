from modeltranslation.translator import register, TranslationOptions

from info.models import (AboutImageModel, InfoModel, TeamModel, HistoryModel,
                         BlogImageModel, CategoryModel,
                         PostTagModel, PostModel)


@register(AboutImageModel)
class AboutImageTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(InfoModel)
class InfoTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


@register(TeamModel)
class TeamTranslationOptions(TranslationOptions):
    fields = ('position', 'name', 'description',)


@register(HistoryModel)
class HistoryTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


@register(BlogImageModel)
class BlogImageTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(CategoryModel)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(PostTagModel)
class PostTagTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(PostModel)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)
