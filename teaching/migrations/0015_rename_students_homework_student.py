# Generated by Django 5.0.1 on 2024-02-08 00:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teaching', '0014_remove_homework_students_homework_students'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homework',
            old_name='students',
            new_name='student',
        ),
    ]