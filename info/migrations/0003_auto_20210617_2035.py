# Generated by Django 3.2.4 on 2021-06-17 15:35

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_auto_20210616_2316'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutAuthorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='about_the_author_images')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'about author',
                'verbose_name_plural': 'about author',
            },
        ),
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=10)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
            },
        ),
        migrations.CreateModel(
            name='ExtraParagraphModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'extra paragraph',
                'verbose_name_plural': 'extra paragraph',
            },
        ),
        migrations.CreateModel(
            name='PostTagModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'post tag',
                'verbose_name_plural': 'post tags',
            },
        ),
        migrations.AddField(
            model_name='postmodel',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='posts', to='info.categorymodel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='postmodel',
            name='tags',
            field=models.ManyToManyField(related_name='posts', to='info.PostTagModel'),
        ),
    ]