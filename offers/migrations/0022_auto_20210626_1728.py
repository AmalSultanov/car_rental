# Generated by Django 3.2 on 2021-06-26 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0021_auto_20210626_1717'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doormodel',
            old_name='doors',
            new_name='amount',
        ),
        migrations.RenameField(
            model_name='seatmodel',
            old_name='seats',
            new_name='amount',
        ),
        migrations.RenameField(
            model_name='transmissionmodel',
            old_name='transmission',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='typemodel',
            old_name='type',
            new_name='title',
        ),
    ]