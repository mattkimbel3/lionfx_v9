# Generated by Django 3.2.16 on 2023-11-15 22:32

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('forex', '0077_optiontrade_assets_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='cryptopair',
            name='chart_data',
            field=jsonfield.fields.JSONField(blank=True, default=list, null=True),
        ),
    ]
