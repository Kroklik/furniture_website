# Generated by Django 5.0.1 on 2024-01-22 15:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digital', '0002_product_edited_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='digital.brand'),
        ),
        migrations.AddField(
            model_name='product',
            name='color_code',
            field=models.TextField(blank=True, default='#000000', null=True, verbose_name='Код цвета'),
        ),
        migrations.AddField(
            model_name='product',
            name='color_name',
            field=models.TextField(blank=True, default='Желтый', null=True, verbose_name='Цвет'),
        ),
    ]