# Generated by Django 4.2.1 on 2023-08-06 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_cart_product_name_alter_cart_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='user',
        ),
    ]
