from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.translation import gettext_lazy as _


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.__class__.objects.exclude(id=self.id).delete()
        super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        try:
            return cls.objects.get()
        except cls.DoesNotExist:
            return cls()


class AboutImageModel(SingletonModel):
    image = models.ImageField(upload_to='about_bg_image',
                              verbose_name=_('image'))
    title = models.CharField(max_length=30, verbose_name=_('title'))

    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('about home image')
        verbose_name_plural = _('about home image')


class InfoModel(SingletonModel):
    title = models.CharField(max_length=30, verbose_name=_('title'))
    description = RichTextUploadingField(verbose_name=_('description'))
    image = models.ImageField(upload_to='info_image',
                              verbose_name=_('image'))

    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('info')
        verbose_name_plural = _('info')


class TeamModel(models.Model):
    image = models.ImageField(upload_to='info_image',
                              verbose_name=_('image'))
    position = models.CharField(max_length=20,
                                verbose_name=_('position'))
    name = models.CharField(max_length=20, verbose_name=_('name'))
    description = RichTextUploadingField(verbose_name=_('description'))

    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('created_at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('team')
        verbose_name_plural = _('team')


class HistoryModel(SingletonModel):
    image = models.ImageField(upload_to='history_image',
                              verbose_name=_('title'))
    title = models.CharField(max_length=20, verbose_name=_('title'))
    description = RichTextUploadingField(verbose_name=_('description'))

    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('history')
        verbose_name_plural = _('history')


class BlogImageModel(SingletonModel):
    image = models.ImageField(upload_to='blog_bg_image',
                              verbose_name=_('image'))
    title = models.CharField(max_length=30, verbose_name=_('title'))

    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('blog home image')
        verbose_name_plural = _('blog home image')


class CategoryModel(models.Model):
    title = models.CharField(max_length=20, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')


class PostTagModel(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('post tag')
        verbose_name_plural = _('post tags')


class PostModel(models.Model):
    image = models.ImageField(upload_to='posts_images',
                              verbose_name=_('image'))
    title = models.CharField(max_length=100, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('created_at'))
    content = RichTextUploadingField(verbose_name=_('content'))
    category = models.ForeignKey(
        CategoryModel,
        on_delete=models.PROTECT,
        related_name='posts',
        verbose_name=_('category')
    )
    tags = models.ManyToManyField(
        PostTagModel,
        related_name='posts',
        verbose_name=_('tags')
    )

    def get_comments(self):
        return self.comments.order_by('-created_at')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')


class CommentModel(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('name'))
    image = models.ImageField(upload_to='user_comment_images',
                              verbose_name=_('image'))
    comment = models.TextField(verbose_name=_('comment'))
    post = models.ForeignKey(
        PostModel,
        related_name='comments',
        on_delete=models.CASCADE,
        verbose_name=_('post')
    )

    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('created_at'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')
