# Generated by Django 3.2.16 on 2023-11-23 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forex', '0092_alter_transaction_trader'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.CharField(max_length=10),
        ),
    ]
