# Generated by Django 4.2.3 on 2023-08-27 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_mobiles_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sabadekharid',
            fields=[
                ('idnumber', models.IntegerField(primary_key=True, serialize=False)),
                ('brand', models.CharField(max_length=7)),
                ('manufacturedate', models.CharField(max_length=7)),
                ('picture', models.ImageField(blank=True, upload_to='images/')),
                ('price', models.IntegerField(default=0)),
                ('quantity', models.IntegerField(default=0)),
                ('totalprice', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='mobiles',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mobiles',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
