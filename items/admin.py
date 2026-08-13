from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "status",
        "category",
        "location",
        "user",
        "date",
    )

    search_fields = (
        "title",
        "location",
        "category",
    )

    list_filter = (
        "status",
        "category",
    )