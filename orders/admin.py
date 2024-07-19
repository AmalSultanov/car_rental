from django.contrib import admin

from orders.models import OrderModel


@admin.register(OrderModel)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone',
                    'email', 'date_from', 'date_to']
    list_filter = ['first_name', 'last_name', 'phone',
                   'email', 'date_from', 'date_to']
    search_fields = ['first_name', 'last_name', 'phone',
                     'email', 'date_from', 'date_to']
