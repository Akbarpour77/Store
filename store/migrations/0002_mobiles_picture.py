# Generated by Django 4.2.3 on 2023-08-19 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobiles',
            name='picture',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
