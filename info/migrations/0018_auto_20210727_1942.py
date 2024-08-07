# Generated by Django 3.2.5 on 2021-07-27 14:42

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0017_delete_extraparagraphmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutimagemodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_at'),
        ),
        migrations.AlterField(
            model_name='aboutimagemodel',
            name='image',
            field=models.ImageField(upload_to='about_bg_image', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='aboutimagemodel',
            name='title',
            field=models.CharField(max_length=30, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='blogimagemodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_at'),
        ),
        migrations.AlterField(
            model_name='blogimagemodel',
            name='image',
            field=models.ImageField(upload_to='blog_bg_image', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='blogimagemodel',
            name='title',
            field=models.CharField(max_length=30, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='categorymodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_at'),
        ),
        migrations.AlterField(
            model_name='categorymodel',
            name='title',
            field=models.CharField(max_length=20, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='commentmodel',
            name='comment',
            field=models.TextField(verbose_name='comment'),
        ),
        migrations.AlterField(
            model_name='commentmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_at'),
        ),
        migrations.AlterField(
            model_name='commentmodel',
            name='image',
            field=models.ImageField(upload_to='user_comment_images', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='commentmodel',
            name='name',
            field=models.CharField(max_length=50, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='commentmodel',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='info.postmodel', verbose_name='post'),
        ),
        migrations.AlterField(
            model_name='historymodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_at'),
        ),
        migrations.AlterField(
            model_name='historymodel',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='historymodel',
            name='image',
            field=models.ImageField(upload_to='history_image', verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='historymodel',
            name='title',
            field=models.CharField(max_length=20, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='infomodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_at'),
        ),
        migrations.AlterField(
            model_name='infomodel',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='infomodel',
            name='image',
            field=models.ImageField(upload_to='info_image', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='infomodel',
            name='title',
            field=models.CharField(max_length=30, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='info.categorymodel', verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_at'),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='image',
            field=models.ImageField(upload_to='posts_images', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='tags',
            field=models.ManyToManyField(related_name='posts', to='info.PostTagModel', verbose_name='tags'),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='title',
            field=models.CharField(max_length=100, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='posttagmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_at'),
        ),
        migrations.AlterField(
            model_name='posttagmodel',
            name='title',
            field=models.CharField(max_length=50, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='teammodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_at'),
        ),
        migrations.AlterField(
            model_name='teammodel',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='teammodel',
            name='image',
            field=models.ImageField(upload_to='info_image', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='teammodel',
            name='name',
            field=models.CharField(max_length=20, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='teammodel',
            name='position',
            field=models.CharField(max_length=20, verbose_name='position'),
        ),
    ]
