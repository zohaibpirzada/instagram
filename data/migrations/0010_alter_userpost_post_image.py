# Generated by Django 5.0.1 on 2024-04-18 17:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("data", "0009_alter_userpost_post_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userpost",
            name="post_image",
            field=models.ImageField(null=True, upload_to="post_image"),
        ),
    ]
