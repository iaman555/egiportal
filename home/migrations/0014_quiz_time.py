# Generated by Django 3.2.8 on 2021-11-12 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_quiz_serial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='time',
            field=models.TimeField(default=1),
            preserve_default=False,
        ),
    ]
