from django.db import models

from l10n_apps.models import L10App
from utils.models import GlobalModel


class L10AppTranslation(GlobalModel):
    """L10 App Translations model.

    Saves translations as `json` format, to use easy in frontend applications.
    See
    [this](https://docs.djangoproject.com/en/4.1/ref/models/fields/#jsonfield)
    to get more useful info about `JSONField`.
    """

    bundle_id = models.ForeignKey(
        L10App,
        on_delete=models.CASCADE,
        verbose_name=("App bundle id"),
        related_name="apps",
        related_query_name="apps",
    )
    locale = models.CharField(max_length=4, null=False)
    translation = models.JSONField(blank=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
        null=True,
    )
