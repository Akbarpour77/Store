# Generated by Django 4.2.3 on 2023-08-08 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginregister', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, upload_to='profile_pictures'),
        ),
    ]
