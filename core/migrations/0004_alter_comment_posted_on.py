# Generated by Django 4.0 on 2022-01-12 05:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_comment_author_alter_comment_posted_on_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='posted_on',
            field=models.DateField(default=datetime.datetime(2022, 1, 12, 5, 59, 39, 942099, tzinfo=utc)),
        ),
    ]
