# Generated by Django 2.2.8 on 2020-05-09 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_merge_20200509_1623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
