# Generated by Django 2.1.7 on 2019-03-07 15:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("core", "0002_auto_20190307_1454")]

    operations = [
        migrations.CreateModel(
            name="SMS",
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
                ("number", models.CharField(max_length=255)),
                ("message", models.TextField()),
                ("is_sent", models.BooleanField(blank=True, default=False)),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
        )
    ]