# Generated by Django 4.0.2 on 2022-03-09 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_rename_contactnummber_user_contactnumber'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='customer',
            table='customer',
        ),
        migrations.AlterModelTable(
            name='role',
            table='role',
        ),
        migrations.AlterModelTable(
            name='serviceprovider',
            table='service_provider',
        ),
    ]