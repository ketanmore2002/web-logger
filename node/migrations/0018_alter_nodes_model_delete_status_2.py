# Generated by Django 4.1.5 on 2023-01-12 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('node', '0017_alter_nodes_model_delete_status_2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nodes_model',
            name='delete_status_2',
            field=models.CharField(blank=True, choices=[('Deleted', 'Deleted'), ('Restore', 'Restore')], default='', max_length=300, null=True, verbose_name='Delete Status'),
        ),
    ]
