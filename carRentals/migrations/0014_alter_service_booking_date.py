# Generated by Django 4.0.4 on 2022-08-17 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carRentals', '0013_service_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service_booking',
            name='date',
            field=models.CharField(max_length=30),
        ),
    ]
