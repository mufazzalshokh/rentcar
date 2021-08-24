# Generated by Django 3.2.4 on 2021-08-24 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20210824_2333'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='brand',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='products', to='shop.brandmodel'),
            preserve_default=False,
        ),
    ]
