# Generated by Django 4.1.5 on 2023-08-04 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('node', '0025_time_stamp_date_rig_time_stamp_time_rig'),
    ]

    operations = [
        migrations.AddField(
            model_name='node_health',
            name='parameter',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
