# Generated by Django 3.2.5 on 2021-08-08 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0048_carimagemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmodel',
            name='real_price',
            field=models.FloatField(default=0, verbose_name='real price'),
        ),
    ]
