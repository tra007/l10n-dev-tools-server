# Generated by Django 4.1.7 on 2023-02-24 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("l10n_app_translations", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="l10apptranslation",
            name="deleted_at",
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
