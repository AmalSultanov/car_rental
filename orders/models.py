from django.db import models
from django.utils.translation import gettext_lazy as _


class OrderModel(models.Model):
    first_name = models.CharField(max_length=50,
                                  verbose_name=_('first_name'))
    last_name = models.CharField(max_length=50,
                                 verbose_name=_('last_name'))
    phone = models.CharField(max_length=50, verbose_name=_('phone'))
    email = models.EmailField(verbose_name=_('email'))
    date_from = models.DateTimeField(null=True,
                                     verbose_name=_('date_from'))
    date_to = models.DateTimeField(null=True,
                                   verbose_name=_('date_to'))

    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('created_at'))

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = _('order')
        verbose_name_plural = _('orders')
