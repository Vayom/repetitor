# Generated by Django 5.0.1 on 2024-02-10 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teaching', '0017_homework_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='homework',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]