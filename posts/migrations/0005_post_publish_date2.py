# Generated by Django 4.2 on 2023-11-06 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_remove_post_publish_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='publish_date2',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
