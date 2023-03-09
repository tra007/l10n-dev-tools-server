# Generated by Django 4.1.7 on 2023-03-09 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="L10Apps",
            fields=[
                (
                    "deleted_at",
                    models.DateTimeField(blank=True, default=None, null=True),
                ),
                (
                    "bundle_id",
                    models.CharField(
                        db_index=True, max_length=20, primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                ("descriptions", models.CharField(blank=True, max_length=60)),
                ("created_at", models.DateTimeField(auto_now=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                "db_table": "l10apps",
            },
        ),
    ]
