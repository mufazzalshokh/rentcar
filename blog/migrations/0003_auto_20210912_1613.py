# Generated by Django 3.2.4 on 2021-09-12 11:13

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_commentmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='extra_content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='postmodel',
            name='long_description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='postmodel',
            name='short_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='postmodel',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos/%y'),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='availability',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
