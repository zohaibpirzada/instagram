# Generated by Django 5.0.1 on 2024-04-19 09:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("data", "0018_alter_pic_image_alter_pic_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pic",
            name="image",
            field=models.ImageField(blank=True, default=2, upload_to="pic"),
            preserve_default=False,
        ),
    ]