# Generated by Django 4.1.5 on 2023-07-03 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('node', '0021_remove_nodes_model_activate'),
    ]

    operations = [
        migrations.CreateModel(
            name='task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, default='incomplete', max_length=300, null=True)),
            ],
        ),
    ]
