# Generated by Django 4.2.4 on 2023-12-25 01:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("commentapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="created_at",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]