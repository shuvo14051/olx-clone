# Generated by Django 2.2 on 2020-08-04 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20200804_1436'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productimages',
            options={'verbose_name': 'Product Image', 'verbose_name_plural': 'Product Images'},
        ),
    ]