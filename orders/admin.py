from django.contrib import admin

from .models import Order, OrderBook
from users.models import User



class OrderBookInline(admin.TabularInline):
    model = OrderBook
    raw_id_fields = ['book']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'id', 'address', 'postal_code', 'city', 'state', 'paid',
                   'comment', 'phone_number', 'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderBookInline]

 