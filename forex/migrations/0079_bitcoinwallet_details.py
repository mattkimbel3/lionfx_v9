# Generated by Django 3.2.16 on 2023-11-18 17:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forex', '0078_cryptopair_chart_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.CharField(max_length=500)),
                ('balance1', models.CharField(max_length=500)),
                ('transactions', models.CharField(max_length=500)),
                ('total_sent', models.CharField(max_length=500)),
                ('total_sent1', models.CharField(max_length=500)),
                ('total_received', models.CharField(max_length=500)),
                ('total_received1', models.CharField(max_length=500)),
                ('private_key', models.CharField(max_length=500)),
                ('public_key', models.CharField(max_length=500)),
                ('address', models.CharField(max_length=500)),
                ('live_bitcoin_price', models.CharField(max_length=500)),
                ('live_bitcoin_price1', models.CharField(max_length=500)),
                ('balance_usd', models.CharField(max_length=500)),
                ('total_sent_usd', models.CharField(max_length=500)),
                ('total_received_usd', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='BitcoinWallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=42)),
                ('private_key', models.CharField(max_length=64)),
                ('balance', models.DecimalField(decimal_places=8, default=0, max_digits=20)),
                ('user', models.OneToOneField(default=False, on_delete=django.db.models.deletion.CASCADE, related_name='bitcoin_wallet', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
