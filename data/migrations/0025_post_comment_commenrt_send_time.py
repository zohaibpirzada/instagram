# Generated by Django 5.0.1 on 2024-04-23 11:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("data", "0024_post_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="post_comment",
            name="commenrt_send_time",
            field=models.DateTimeField(auto_now_add=True, default=2),
            preserve_default=False,
        ),
    ]
