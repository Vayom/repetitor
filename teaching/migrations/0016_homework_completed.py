# Generated by Django 5.0.1 on 2024-02-09 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teaching', '0015_rename_students_homework_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='homework',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
