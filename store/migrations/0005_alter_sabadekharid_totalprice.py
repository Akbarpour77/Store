# Generated by Django 4.2.3 on 2023-08-29 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_sabadekharid_mobiles_price_mobiles_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sabadekharid',
            name='totalprice',
            field=models.IntegerField(default=0),
        ),
    ]
