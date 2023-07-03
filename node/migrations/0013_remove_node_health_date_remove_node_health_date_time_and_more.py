# Generated by Django 4.1.5 on 2023-06-24 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('node', '0012_time_stamp_node_health_date_node_health_date_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='node_health',
            name='date',
        ),
        migrations.RemoveField(
            model_name='node_health',
            name='date_time',
        ),
        migrations.RemoveField(
            model_name='node_health',
            name='time',
        ),
        migrations.AddField(
            model_name='time_stamp',
            name='date',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='time_stamp',
            name='date_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='time_stamp',
            name='time',
            field=models.TimeField(auto_now=True, null=True),
        ),
    ]