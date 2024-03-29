# Generated by Django 4.2.1 on 2023-05-16 10:21

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):
    dependencies = [
        ("taggit", "0005_auto_20220424_2025"),
        ("pages", "0006_pagemodel_map"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pagemodel",
            name="images",
            field=wagtail.fields.StreamField(
                [
                    (
                        "images",
                        wagtail.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock()),
                    )
                ],
                blank=True,
                null=True,
                use_json_field=True,
            ),
        ),
        migrations.AlterField(
            model_name="pagetag",
            name="tag",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="%(app_label)s_%(class)s_items",
                to="taggit.tag",
            ),
        ),
    ]
