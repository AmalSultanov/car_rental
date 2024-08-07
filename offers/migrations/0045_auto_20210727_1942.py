# Generated by Django 3.2.5 on 2021-07-27 14:42

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0044_rename_year_yearmodel_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brandmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_at'),
        ),
        migrations.AlterField(
            model_name='brandmodel',
            name='title',
            field=models.CharField(max_length=20, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cars', to='offers.brandmodel', verbose_name='brand'),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='cars', to='offers.colormodel', verbose_name='color'),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_at'),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='drive',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cars', to='offers.drivemodel', verbose_name='drive'),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='fuel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cars', to='offers.fuelmodel', verbose_name='fuel'),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='image',
            field=models.ImageField(upload_to='car_images', verbose_name='images'),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='power',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cars', to='offers.powermodel', verbose_name='power'),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='title',
            field=models.CharField(max_length=40, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='transmission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cars', to='offers.transmissionmodel', verbose_name='transmission'),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cars', to='offers.typemodel', verbose_name='type'),
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cars', to='offers.yearmodel', verbose_name='year'),
        ),
        migrations.AlterField(
            model_name='carsimagemodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_at'),
        ),
        migrations.AlterField(
            model_name='carsimagemodel',
            name='image',
            field=models.ImageField(upload_to='cars_bg_image', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='carsimagemodel',
            name='title',
            field=models.CharField(max_length=30, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='colormodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_at'),
        ),
        migrations.AlterField(
            model_name='colormodel',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='drivemodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_at'),
        ),
        migrations.AlterField(
            model_name='drivemodel',
            name='title',
            field=models.CharField(max_length=15, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='fuelmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_at'),
        ),
        migrations.AlterField(
            model_name='fuelmodel',
            name='title',
            field=models.CharField(max_length=20, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='powermodel',
            name='amount',
            field=models.PositiveIntegerField(verbose_name='amount'),
        ),
        migrations.AlterField(
            model_name='powermodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_at'),
        ),
        migrations.AlterField(
            model_name='servicesimagemodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_at'),
        ),
        migrations.AlterField(
            model_name='servicesimagemodel',
            name='image',
            field=models.ImageField(upload_to='services_bg_image', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='servicesimagemodel',
            name='title',
            field=models.CharField(max_length=30, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='transmissionmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_at'),
        ),
        migrations.AlterField(
            model_name='transmissionmodel',
            name='title',
            field=models.CharField(max_length=50, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='typemodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_at'),
        ),
        migrations.AlterField(
            model_name='typemodel',
            name='title',
            field=models.CharField(max_length=15, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='yearmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_at'),
        ),
        migrations.AlterField(
            model_name='yearmodel',
            name='title',
            field=models.PositiveIntegerField(verbose_name='title'),
        ),
    ]
