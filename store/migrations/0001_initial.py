# Generated by Django 4.2.3 on 2023-08-16 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mobiles',
            fields=[
                ('idnumber', models.IntegerField(primary_key=True, serialize=False)),
                ('brand', models.CharField(max_length=7)),
                ('manufacturedate', models.CharField(max_length=7)),
                ('cpu', models.CharField(max_length=7)),
                ('gpu', models.CharField(max_length=7)),
                ('monitor', models.CharField(max_length=7)),
                ('monitorsize', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
