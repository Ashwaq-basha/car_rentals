# Generated by Django 4.0.4 on 2022-08-10 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carRentals', '0005_alter_help_message_alter_help_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='help',
            name='Email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='help',
            name='name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
