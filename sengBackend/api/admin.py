from django.contrib import admin

from .models import Record


# Register your models here.
@admin.register(Record)
class RecordModel(admin.ModelAdmin):
    list_filter = "illness", "description"
    list_display = "illness", "description"
