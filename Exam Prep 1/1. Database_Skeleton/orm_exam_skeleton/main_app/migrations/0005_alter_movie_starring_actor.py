# Generated by Django 4.2.4 on 2023-11-25 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_movie_actors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='starring_actor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.actor'),
        ),
    ]