# Generated by Django 5.0.1 on 2024-04-15 09:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("data", "0003_profile_follow_alter_profile_profile_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="follow",
            field=models.ManyToManyField(
                blank=True, related_name="following", to="data.profile"
            ),
        ),
    ]
