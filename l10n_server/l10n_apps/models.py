from django.db import models

from utils.models import GlobalModel


class L10App(GlobalModel):
    bundle_id = models.CharField(
        primary_key=True,
        max_length=20,
        db_index=True,
    )  # app_243fr#d
    name = models.CharField(max_length=30)  # Application-name
    descriptions = models.CharField(max_length=60, blank=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
        null=True,
    )

    def __str__(self):
        return self.name
