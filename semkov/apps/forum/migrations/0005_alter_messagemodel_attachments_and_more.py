# Generated by Django 4.2.1 on 2023-05-16 10:21

from django.db import migrations
import wagtail.blocks
import wagtail.documents.blocks
import wagtail.fields


class Migration(migrations.Migration):
    dependencies = [
        ("forum", "0004_auto_20190306_1239"),
    ]

    operations = [
        migrations.AlterField(
            model_name="messagemodel",
            name="attachments",
            field=wagtail.fields.StreamField(
                [
                    (
                        "attachments",
                        wagtail.blocks.ListBlock(
                            wagtail.documents.blocks.DocumentChooserBlock()
                        ),
                    )
                ],
                blank=True,
                null=True,
                use_json_field=True,
            ),
        ),
        migrations.AlterField(
            model_name="threadmodel",
            name="attachments",
            field=wagtail.fields.StreamField(
                [
                    (
                        "attachments",
                        wagtail.blocks.ListBlock(
                            wagtail.documents.blocks.DocumentChooserBlock()
                        ),
                    )
                ],
                blank=True,
                null=True,
                use_json_field=True,
            ),
        ),
    ]
