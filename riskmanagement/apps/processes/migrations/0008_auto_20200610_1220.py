# Generated by Django 3.0.4 on 2020-06-10 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0007_processtype_is_default'),
    ]

    operations = [
        migrations.AddField(
            model_name='process',
            name='aim',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='process',
            name='description',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
    ]
