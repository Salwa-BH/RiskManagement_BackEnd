# Generated by Django 3.0.4 on 2021-02-17 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0011_remove_player_function'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]