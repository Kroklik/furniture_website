# Generated by Django 5.0.1 on 2024-02-18 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('digital', '0017_orderproduct_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproduct',
            name='user',
        ),
    ]
