# Generated by Django 4.2.1 on 2023-08-06 13:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0002_product_is_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('thambnali', models.URLField()),
                ('quantity', models.IntegerField(default=1)),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_name', to='products.product')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_name', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]