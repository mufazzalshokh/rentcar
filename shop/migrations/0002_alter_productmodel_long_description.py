# Generated by Django 3.2.4 on 2021-08-24 18:06

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='long_description',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
