# Generated by Django 4.0.4 on 2022-08-10 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carRentals', '0004_rename_contact_help'),
    ]

    operations = [
        migrations.AlterField(
            model_name='help',
            name='Message',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='help',
            name='Subject',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
