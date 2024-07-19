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


class HomeImageModel(SingletonModel):
    image = models.ImageField(upload_to='home_bg_image',
                              verbose_name=_('image'))
    title = models.CharField(max_length=60, verbose_name=_('title'))

    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('home image')
        verbose_name_plural = _('home image')


class ContactImageModel(SingletonModel):
    image = models.ImageField(upload_to='contact_bg_image',
                              verbose_name=_('image'))
    title = models.CharField(max_length=30, verbose_name=_('title'))

    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('contact home image')
        verbose_name_plural = _('contacts home image')


class ContactModel(models.Model):
    first_name = models.CharField(max_length=255,
                                  verbose_name=_('first_name'))
    last_name = models.CharField(max_length=255,
                                 verbose_name=_('last_name'))
    email = models.EmailField(verbose_name=_('email'))
    message = models.TextField(verbose_name=_('message'))

    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('created_at'))

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = _('contact')
        verbose_name_plural = _('contacts')


class ContactInfoModel(SingletonModel):
    address = models.CharField(max_length=100, verbose_name=_('address'))
    phone = models.CharField(max_length=50, verbose_name=_('phone'))
    email = models.EmailField(verbose_name=_('email'))

    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('created_at'))

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = _('contact info')
        verbose_name_plural = _('contacts info')
