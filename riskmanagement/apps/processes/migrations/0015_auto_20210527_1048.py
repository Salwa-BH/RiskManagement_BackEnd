# Generated by Django 3.0.4 on 2021-05-27 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0014_statusprocess'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process',
            name='status',
            field=models.TextField(default='Empty', max_length=30),
        ),
    ]
