# Generated by Django 3.0.4 on 2021-12-25 10:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('permissions', '0005_role_confirmation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userassign',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]