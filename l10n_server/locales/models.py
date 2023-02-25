from django.db import models

from repositories.models import L10Apps
from utils.models import GlobalModel


class Locales(GlobalModel):
    """L10 App Translations model.

    Saves translations as `json` format, to use easy in frontend applications.
    See
    [this](https://docs.djangoproject.com/en/4.1/ref/models/fields/#jsonfield)
    to get more useful info about `JSONField`.
    """

    bundle_id = models.ForeignKey(
        L10Apps,
        on_delete=models.CASCADE,
        verbose_name=("App bundle id"),
        related_name="apps",
        related_query_name="apps",
    )
    name = models.CharField(max_length=4, null=False)
    translation = models.JSONField(blank=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
        null=True,
    )

    class Meta:
        db_table = "locales"
