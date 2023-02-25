from django.contrib import admin

from locales.models import *


@admin.register(Locales)
class Locales(admin.ModelAdmin):
    list_display = [
        "id",
        "bundle_id",
        "name",
        "translation",
        "created_at",
        "updated_at",
        "deleted_at",
    ]
    ordering = ["id", "bundle_id"]
