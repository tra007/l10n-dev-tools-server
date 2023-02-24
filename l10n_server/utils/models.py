from django.db import models

from django.utils import timezone


class GlobalModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)


class GlobalModel(models.Model):
    """Global Model.

    Manages important parameters in Entities Models.

    ## Functionalities

    - Delete an object: `Model.soft_delete()`
    - Restore an object: `Model.restore()`
    - Return all data that's not deleted: `Model.all_objects.all()`
    """

    deleted_at = models.DateTimeField(null=True, default=None)
    objects = GlobalModelManager()
    all_objects = models.Manager()

    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.deleted_at = None
        self.save()

    class Meta:
        abstract = True
