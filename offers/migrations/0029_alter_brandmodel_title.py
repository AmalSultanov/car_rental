# Generated by Django 3.2 on 2021-06-27 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0028_auto_20210627_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brandmodel',
            name='title',
            field=models.CharField(max_length=20),
        ),
    ]
