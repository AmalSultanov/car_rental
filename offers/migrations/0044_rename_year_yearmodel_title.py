# Generated by Django 3.2.5 on 2021-07-16 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0043_auto_20210716_1358'),
    ]

    operations = [
        migrations.RenameField(
            model_name='yearmodel',
            old_name='year',
            new_name='title',
        ),
    ]