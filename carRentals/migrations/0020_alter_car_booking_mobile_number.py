# Generated by Django 4.0.4 on 2022-08-23 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carRentals', '0019_rename_card_number_car_booking_card_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car_booking',
            name='mobile_number',
            field=models.CharField(max_length=10, null=True),
        ),
    ]