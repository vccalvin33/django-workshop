# Generated by Django 4.1.2 on 2022-10-28 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='task_owners',
            new_name='task_owner',
        ),
    ]
