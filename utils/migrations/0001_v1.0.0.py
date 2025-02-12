# Generated by Django 2.2.7 on 2019-11-13 21:14

import django.contrib.postgres.fields.jsonb
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import utils.forms.fields


class Migration(migrations.Migration):
    replaces = [
        ("utils", "0001_initial"),
        ("utils", "0002_auto_20180329_2146"),
        ("utils", "0003_auto_20181112_2150"),
        ("utils", "0004_auto_20181208_2202"),
        ("utils", "0005_tag_taggeditem"),
    ]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("contenttypes", "0002_remove_content_type_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="ObjectChange",
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
                ("time", models.DateTimeField(auto_now_add=True)),
                ("user_name", models.CharField(editable=False, max_length=150)),
                ("request_id", models.UUIDField(editable=False)),
                (
                    "action",
                    models.PositiveSmallIntegerField(
                        choices=[(1, "Created"), (2, "Updated"), (3, "Deleted")]
                    ),
                ),
                ("changed_object_id", models.PositiveIntegerField()),
                (
                    "related_object_id",
                    models.PositiveIntegerField(blank=True, null=True),
                ),
                ("object_repr", models.CharField(editable=False, max_length=256)),
                (
                    "object_data",
                    django.contrib.postgres.fields.jsonb.JSONField(editable=False),
                ),
                (
                    "changed_object_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="contenttypes.ContentType",
                    ),
                ),
                (
                    "related_object_type",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="contenttypes.ContentType",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="changes",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"ordering": ["-time"]},
        ),
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
