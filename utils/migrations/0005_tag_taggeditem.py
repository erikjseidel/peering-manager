# Generated by Django 2.2.5 on 2019-09-21 18:00

import django.db.models.deletion
from django.db import migrations, models

import utils.forms.fields


class Migration(migrations.Migration):
    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("utils", "0004_auto_20181208_2202"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=100, unique=True, verbose_name="Name"),
                ),
                (
                    "slug",
                    models.SlugField(max_length=100, unique=True, verbose_name="Slug"),
                ),
                ("created", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated", models.DateTimeField(auto_now=True, null=True)),
                (
                    "color",
                    utils.forms.fields.ColorField(default="9e9e9e", max_length=6),
                ),
                ("comments", models.TextField(blank=True, default="")),
            ],
            options={"abstract": False},
        ),
        migrations.CreateModel(
            name="TaggedItem",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "object_id",
                    models.IntegerField(db_index=True, verbose_name="Object id"),
                ),
                (
                    "content_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(app_label)s_%(class)s_tagged_items",
                        to="contenttypes.contenttype",
                        verbose_name="content type",
                    ),
                ),
                (
                    "tag",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(app_label)s_%(class)s_items",
                        to="utils.tag",
                    ),
                ),
            ],
            options={"index_together": {("content_type", "object_id")}},
        ),
    ]
