# Generated by Django 2.2.1 on 2019-06-14 19:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0003_auto_20190524_1335'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('use_default_address', models.BooleanField(default=False)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('phone', models.CharField(max_length=25)),
                ('payment_method', models.CharField(choices=[('Paypal', 'Paypal'), ('Card', 'Card'), ('Cash', 'Cash'), ('Qiwi', 'Qiwi')], default='Card', max_length=25)),
                ('delivery_method', models.CharField(choices=[('Standart', 'Standart delivery'), ('Next day', 'Next day delivery')], default='Standart', max_length=25)),
                ('status', models.CharField(choices=[('Submitted', 'Submitted'), ('Approved', 'Approved'), ('In progress', 'In progress'), ('Complete', 'Complete')], default='Submitted', max_length=25)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='cart.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
