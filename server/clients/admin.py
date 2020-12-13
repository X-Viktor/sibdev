from django.contrib import admin

from .models import Deal, Csv


@admin.register(Deal)
class DealsAdmin(admin.ModelAdmin):
    list_display = ['customer', 'item', 'total', 'quantity', 'date']


@admin.register(Csv)
class CsvAdmin(admin.ModelAdmin):
    list_display = ['id', 'activated']
