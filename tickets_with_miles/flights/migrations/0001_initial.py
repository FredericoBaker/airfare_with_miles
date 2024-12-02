# Generated by Django 5.1.3 on 2024-11-28 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('iata_code', models.CharField(max_length=3, unique=True)),
                ('state_code', models.CharField(max_length=3)),
                ('country_code', models.CharField(max_length=3)),
                ('country_name', models.CharField(max_length=255)),
            ],
        ),
    ]