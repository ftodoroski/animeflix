# Generated by Django 4.0 on 2022-05-11 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_program_runtime'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_num',
            field=models.IntegerField(default=1),
        ),
    ]