# Generated by Django 5.0.1 on 2024-02-22 11:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlantModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plant_type', models.CharField(choices=[('Outdoor Plants', 'Outdoor Plants'), ('Indoor Plants', 'Indoor Plants')], max_length=14, verbose_name='Plant Type')),
                ('plant_name', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='Name')),
                ('image_url', models.URLField(verbose_name='Image URL')),
                ('description', models.TextField(verbose_name='Description')),
                ('price', models.FloatField(verbose_name='Price')),
            ],
        ),
    ]
