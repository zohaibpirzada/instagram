# Generated by Django 5.0.1 on 2024-04-23 11:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("data", "0029_delete_pic"),
    ]

    operations = [
        migrations.AddField(
            model_name="post_comment",
            name="commenrt_send_time",
            field=models.DateField(auto_now_add=True, default="5:10"),
            preserve_default=False,
        ),
    ]