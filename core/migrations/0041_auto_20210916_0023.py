# Generated by Django 3.2.6 on 2021-09-16 00:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0040_alter_organization_supervisors'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='organization',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.organization'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='organizations', related_query_name='org', to='core.Tag'),
        ),
    ]
