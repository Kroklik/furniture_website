# Generated by Django 5.0.1 on 2024-02-10 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digital', '0010_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description_all',
            field=models.TextField(blank=True, null=True, verbose_name='Описание для страницы о товаре'),
        ),
    ]