# Generated by Django 5.0.1 on 2024-02-07 23:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teaching', '0011_teacher_students_request'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RequestTeaching',
        ),
    ]
