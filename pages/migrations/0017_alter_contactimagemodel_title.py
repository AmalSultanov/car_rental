# Generated by Django 3.2.4 on 2021-06-20 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0016_homeimagemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactimagemodel',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
