# Generated by Django 3.0.4 on 2020-06-02 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0005_auto_20200602_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process',
            name='status',
            field=models.TextField(default='empty', max_length=30),
        ),
    ]
