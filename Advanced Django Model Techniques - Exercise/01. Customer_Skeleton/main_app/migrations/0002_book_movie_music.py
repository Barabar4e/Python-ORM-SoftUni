# Generated by Django 4.2.4 on 2023-11-21 15:04

from django.db import migrations, models
import main_app.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('genre', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('author', models.CharField(max_length=100, validators=[main_app.validators.author_length_validator])),
                ('isbn', models.CharField(max_length=20, unique=True, validators=[main_app.validators.isbn_length_validator])),
            ],
            options={
                'verbose_name': 'Model Book',
                'verbose_name_plural': 'Models of type - Book',
                'ordering': ['-created_at', 'title'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('genre', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('director', models.CharField(max_length=100, validators=[main_app.validators.director_length_validator])),
            ],
            options={
                'verbose_name': 'Model Movie',
                'verbose_name_plural': 'Models of type - Movie',
                'ordering': ['-created_at', 'title'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('genre', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('artist', models.CharField(max_length=100, validators=[main_app.validators.artist_length_validator])),
            ],
            options={
                'verbose_name': 'Model Music ',
                'verbose_name_plural': 'Models of type - Music',
                'ordering': ['-created_at', 'title'],
                'abstract': False,
            },
        ),
    ]