# Generated by Django 3.2.6 on 2021-09-01 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_event_term'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='schedule_format',
            field=models.CharField(max_length=64),
        ),
    ]
