# Generated by Django 4.0.4 on 2022-08-06 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carRentals', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='Suject',
            new_name='Subject',
        ),
    ]
