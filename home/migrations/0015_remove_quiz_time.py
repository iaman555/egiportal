# Generated by Django 3.2.8 on 2021-11-12 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_quiz_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='time',
        ),
    ]
