# Generated by Django 5.0.1 on 2024-02-04 17:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digital', '0008_alter_favoriteproduct_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brand', to='digital.category', verbose_name='Категория'),
        ),
    ]
