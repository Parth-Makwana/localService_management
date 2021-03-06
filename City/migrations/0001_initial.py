# Generated by Django 4.0.2 on 2022-03-23 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amount', models.IntegerField()),
                ('Transaction', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Payment',
            },
        ),
        migrations.CreateModel(
            name='service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ServiceName', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Service',
            },
        ),
        migrations.CreateModel(
            name='state',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StateName', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'State',
            },
        ),
        migrations.CreateModel(
            name='city',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CityName', models.CharField(max_length=30)),
                ('StateId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='City.state')),
            ],
            options={
                'db_table': 'City',
            },
        ),
    ]
