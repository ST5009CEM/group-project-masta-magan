# Generated by Django 4.0.6 on 2022-07-17 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vechiles', '0002_cheatmodel_vechiletype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cheatmodel',
            name='vechiletype',
        ),
    ]
