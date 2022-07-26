# Generated by Django 4.0.6 on 2022-07-18 05:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinfomodel',
            old_name='product_image',
            new_name='profile_image',
        ),
        migrations.AddField(
            model_name='userinfomodel',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='userinfomodel',
            name='uid',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]