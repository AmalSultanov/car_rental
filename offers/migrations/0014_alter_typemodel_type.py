# Generated by Django 3.2 on 2021-06-22 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0013_auto_20210623_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='typemodel',
            name='type',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
