# Generated by Django 2.2.8 on 2020-10-31 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20201031_2004'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='shipping_address',
            new_name='shipp_address',
        ),
    ]
