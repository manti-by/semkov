# Generated by Django 2.1.7 on 2019-02-15 13:21

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("wagtailcore", "0041_group_collection_permissions_verbose_name_plural")
    ]

    operations = [
        migrations.CreateModel(
            name="PageModel",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.Page",
                    ),
                ),
                (
                    "images",
                    wagtail.fields.StreamField(
                        [
                            (
                                "images",
                                wagtail.blocks.ListBlock(
                                    wagtail.images.blocks.ImageChooserBlock()
                                ),
                            )
                        ],
                        blank=True,
                        null=True,
                    ),
                ),
                ("excerpt", wagtail.fields.RichTextField()),
                ("text", wagtail.fields.RichTextField()),
                ("source", models.URLField()),
            ],
            options={"abstract": False},
            bases=("wagtailcore.page",),
        )
    ]
