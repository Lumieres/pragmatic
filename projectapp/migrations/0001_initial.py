# Generated by Django 4.2.4 on 2023-12-25 14:44

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=20)),
                ("description", models.TextField(max_length=200, null=True)),
                ("image", models.ImageField(upload_to="projects/")),
                ("create_at", models.DateField(auto_now=True)),
            ],
        ),
    ]
