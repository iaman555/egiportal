# Generated by Django 3.2.8 on 2021-11-12 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_remove_quiz_serial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='serial',
            field=models.IntegerField(default=1, verbose_name=models.AutoField(primary_key=True, verbose_name='1')),
            preserve_default=False,
        ),
    ]
