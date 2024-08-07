# Generated by Django 3.2.4 on 2021-06-14 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_fastrentmodel_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='cars_images')),
                ('title', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('type', models.CharField(max_length=20)),
                ('doors', models.IntegerField()),
                ('seats', models.IntegerField()),
                ('transmission', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'car',
                'verbose_name_plural': 'cars',
            },
        ),
    ]
