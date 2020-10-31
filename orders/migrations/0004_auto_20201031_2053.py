# Generated by Django 2.2.8 on 2020-10-31 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0004_auto_20200811_2352'),
        ('orders', '0003_auto_20201031_2031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='shipp_address',
        ),
        migrations.AddField(
            model_name='order',
            name='shipping_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shipping_address', to='addresses.Address'),
        ),
    ]
