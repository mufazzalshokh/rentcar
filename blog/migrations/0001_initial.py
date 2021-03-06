# Generated by Django 3.2.4 on 2021-08-27 17:15

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostTagModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'post tag',
                'verbose_name_plural': 'post tags',
            },
        ),
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
                ('image', models.ImageField(upload_to='posts')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('brand', models.CharField(max_length=20)),
                ('product_code', models.CharField(max_length=30)),
                ('availability', models.CharField(max_length=20)),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('tags', models.ManyToManyField(related_name='posts', to='blog.PostTagModel')),
            ],
            options={
                'verbose_name': 'post',
                'verbose_name_plural': 'posts',
            },
        ),
    ]
