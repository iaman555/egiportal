# Generated by Django 3.2.9 on 2021-11-14 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_remove_quiz_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=50)),
                ('pic', models.ImageField(upload_to='static/images/student_gallry')),
            ],
        ),
    ]
