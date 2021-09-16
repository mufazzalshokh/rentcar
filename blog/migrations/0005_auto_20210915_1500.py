# Generated by Django 3.2.4 on 2021-09-15 10:00

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_postmodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='availability',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='availability'),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='brand',
            field=models.CharField(max_length=20, verbose_name='brand'),
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
            name='extra_content',
            field=models.TextField(blank=True, null=True, verbose_name='extra_content'),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='posts', verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='long_description',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='long_description'),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='price',
            field=models.FloatField(verbose_name='price'),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='product_code',
            field=models.CharField(max_length=30, verbose_name='product_code'),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='quantity',
            field=models.IntegerField(verbose_name='quantity'),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='short_description',
            field=models.TextField(blank=True, null=True, verbose_name='short_description'),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='tags',
            field=models.ManyToManyField(related_name='posts', to='blog.PostTagModel', verbose_name='tags'),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='title',
            field=models.CharField(max_length=512, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos/%y', verbose_name='video'),
        ),
        migrations.AlterField(
            model_name='posttagmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created_at'),
        ),
        migrations.AlterField(
            model_name='posttagmodel',
            name='title',
            field=models.CharField(max_length=20, verbose_name='title'),
        ),
    ]