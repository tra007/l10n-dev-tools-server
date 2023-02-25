from django.contrib import admin

from repositories.models import *


@admin.register(L10Apps)
class L10Apps(admin.ModelAdmin):
    list_display = [
        "bundle_id",
        "name",
        "descriptions",
        "created_at",
        "updated_at",
        "deleted_at",
    ]
    ordering = ["bundle_id"]
