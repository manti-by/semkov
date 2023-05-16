# Generated by Django 2.1.7 on 2019-03-06 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("wagtaildocs", "0010_document_file_hash"),
        ("pages", "0002_pagemodel_menu_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="pagemodel",
            name="document",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtaildocs.Document",
            ),
        ),
        migrations.AddField(
            model_name="pagemodel",
            name="homepage_title",
            field=models.CharField(blank=True, max_length=32),
        ),
        migrations.AddField(
            model_name="pagemodel",
            name="is_homepage",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="pagemodel", name="source", field=models.URLField(blank=True)
        ),
    ]
