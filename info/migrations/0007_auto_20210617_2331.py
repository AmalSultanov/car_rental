# Generated by Django 3.2.4 on 2021-06-17 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0006_auto_20210617_2243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postmodel',
            name='tags',
        ),
        migrations.AddField(
            model_name='postmodel',
            name='tags',
            field=models.ManyToManyField(related_name='posts', to='info.PostTagModel'),
        ),
    ]
