# Generated by Django 4.1.5 on 2023-01-12 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('node', '0015_remove_nodes_model_user_id_alter_nodes_model_co2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='nodes_model',
            name='delete_status_2',
            field=models.CharField(blank=True, choices=[('Deleted', 'Deleted'), ('Restore', 'Restore')], default='Restore', max_length=300, null=True),
        ),
    ]
