# Generated by Django 5.0.1 on 2024-02-05 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teaching', '0006_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='students', to='teaching.student'),
        ),
    ]
