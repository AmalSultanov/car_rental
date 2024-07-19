# Generated by Django 3.2.4 on 2021-06-21 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0005_delete_carmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='car_images')),
                ('title', models.CharField(max_length=35)),
                ('price', models.FloatField()),
                ('type', models.CharField(max_length=15)),
                ('doors', models.IntegerField()),
                ('seats', models.IntegerField()),
                ('transmission', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'car',
                'verbose_name_plural': 'cars',
            },
        ),
    ]