# Generated by Django 3.0.4 on 2021-05-04 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0013_auto_20210226_1705'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusProcess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=1000)),
            ],
        ),
    ]
