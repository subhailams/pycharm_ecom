# Generated by Django 2.2.8 on 2020-08-13 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_orderconfirmation_cart_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderconfirmation',
            name='cart_id',
        ),
        migrations.RemoveField(
            model_name='orderconfirmation',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='orderconfirmation',
            name='update',
        ),
    ]
