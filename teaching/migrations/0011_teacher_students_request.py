# Generated by Django 5.0.1 on 2024-02-06 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teaching', '0010_requestteaching'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='students_request',
            field=models.ManyToManyField(blank=True, related_name='students_request', to='teaching.student'),
        ),
    ]
