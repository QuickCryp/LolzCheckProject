from django.contrib import admin
from .models import Cryptocurrency


admin.site.register(Cryptocurrency)
class CryptocurrencyAdmin(admin.ModelAdmin):
    list_display = ['name', 'symbol', 'price', 'volume', 'change_price']