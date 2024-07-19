from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

UserModel = get_user_model()


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


class ServicesImageModel(SingletonModel):
    image = models.ImageField(upload_to='services_bg_image',
                              verbose_name=_('image'))
    title = models.CharField(max_length=30, verbose_name=_('title'))

    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('services home image')
        verbose_name_plural = _('services home image')


class CarsImageModel(SingletonModel):
    image = models.ImageField(upload_to='cars_bg_image',
                              verbose_name=_('image'))
    title = models.CharField(max_length=30, verbose_name=_('title'))

    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('car home image')
        verbose_name_plural = _('cars home image')


class BrandModel(models.Model):
    title = models.CharField(max_length=20, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('brand')
        verbose_name_plural = _('brands')


class TypeModel(models.Model):
    title = models.CharField(max_length=15, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('type')
        verbose_name_plural = _('types')


class PowerModel(models.Model):
    amount = models.PositiveIntegerField(verbose_name=_('amount'))
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('created_at'))

    def __str__(self):
        return f'{self.amount}'

    class Meta:
        verbose_name = _('power')
        verbose_name_plural = _('power')


class FuelModel(models.Model):
    title = models.CharField(max_length=20, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('fuel')
        verbose_name_plural = _('fuel')


class DriveModel(models.Model):
    title = models.CharField(max_length=15, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('drive')
        verbose_name_plural = _('drive')


class TransmissionModel(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('transmission')
        verbose_name_plural = _('transmissions')


class ColorModel(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('color')
        verbose_name_plural = _('colors')


class YearModel(models.Model):
    title = models.PositiveIntegerField(verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('created_at'))

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = _('year')
        verbose_name_plural = _('years')


class CarModel(models.Model):
    title = models.CharField(max_length=40, verbose_name=_('title'))
    image = models.ImageField(upload_to='car_images',
                              verbose_name=_('images'))
    brand = models.ForeignKey(
        BrandModel,
        on_delete=models.PROTECT,
        related_name='cars',
        verbose_name=_('brand')
    )
    price = models.PositiveIntegerField(verbose_name=_('price'))
    type = models.ForeignKey(
        TypeModel,
        on_delete=models.PROTECT,
        related_name='cars',
        verbose_name=_('type')
    )
    power = models.ForeignKey(
        PowerModel,
        on_delete=models.PROTECT,
        related_name='cars',
        verbose_name=_('power')
    )
    fuel = models.ForeignKey(
        FuelModel,
        on_delete=models.PROTECT,
        related_name='cars',
        verbose_name=_('fuel')
    )
    drive = models.ForeignKey(
        DriveModel,
        on_delete=models.PROTECT,
        related_name='cars',
        verbose_name=_('drive')
    )
    transmission = models.ForeignKey(
        TransmissionModel,
        on_delete=models.PROTECT,
        related_name='cars',
        verbose_name=_('transmission')
    )
    color = models.ForeignKey(
        ColorModel,
        on_delete=models.PROTECT,
        related_name='cars',
        null=True,
        blank=True,
        verbose_name=_('color')
    )
    year = models.ForeignKey(
        YearModel,
        on_delete=models.PROTECT,
        related_name='cars',
        verbose_name=_('year')
    )
    description = RichTextUploadingField(verbose_name=_('description'))

    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('car')
        verbose_name_plural = _('cars')


class CarImageModel(models.Model):
    image = models.ImageField(upload_to='car_images',
                              verbose_name=_('image'))
    car = models.ForeignKey(
        CarModel,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name=_('car')
    )

    def __str__(self):
        return self.car.title

    class Meta:
        verbose_name = _('car image')
        verbose_name_plural = _('car images')
