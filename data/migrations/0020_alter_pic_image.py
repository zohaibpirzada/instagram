# Generated by Django 5.0.1 on 2024-04-19 09:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("data", "0019_alter_pic_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pic",
            name="image",
            field=models.ImageField(upload_to="pic"),
        ),
    ]
