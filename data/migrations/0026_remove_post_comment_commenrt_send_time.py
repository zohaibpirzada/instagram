# Generated by Django 5.0.1 on 2024-04-23 11:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("data", "0025_post_comment_commenrt_send_time"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post_comment",
            name="commenrt_send_time",
        ),
    ]
