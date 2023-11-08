# Generated by Django 4.2.6 on 2023-11-08 13:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="funcao",
            field=models.CharField(
                choices=[
                    ("Tech Lead", "Tech Lead"),
                    ("Dev Front-End", "Dev Front-End"),
                    ("Dev Back-End", "Dev Back-End"),
                    ("Dev Full-Stack", "Dev Full-Stack"),
                ],
                max_length=100,
                null=True,
            ),
        ),
    ]