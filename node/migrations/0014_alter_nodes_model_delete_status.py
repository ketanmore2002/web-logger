# Generated by Django 4.1.5 on 2023-01-11 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('node', '0013_alter_nodes_model_delete_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nodes_model',
            name='delete_status',
            field=models.CharField(blank=True, default='', editable=False, max_length=300, null=True),
        ),
    ]
