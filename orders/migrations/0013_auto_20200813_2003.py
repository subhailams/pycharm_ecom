# Generated by Django 2.2.8 on 2020-08-13 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_auto_20200813_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderconfirmation',
            name='cart_id',
            field=models.IntegerField(blank=True, max_length=120),
        ),
    ]
