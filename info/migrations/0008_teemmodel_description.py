# Generated by Django 3.2.4 on 2021-06-17 18:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0007_auto_20210617_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='teemmodel',
            name='description',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
