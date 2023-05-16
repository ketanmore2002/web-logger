# Generated by Django 4.1.5 on 2023-01-14 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('node', '0019_alter_nodes_model_delete_status_2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nodes_model',
            name='CO2_high',
            field=models.CharField(blank=True, editable=False, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='nodes_model',
            name='CO2_low',
            field=models.CharField(blank=True, editable=False, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='nodes_model',
            name='date',
            field=models.CharField(blank=True, editable=False, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='nodes_model',
            name='humidity_high',
            field=models.CharField(blank=True, editable=False, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='nodes_model',
            name='humidity_low',
            field=models.CharField(blank=True, editable=False, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='nodes_model',
            name='location',
            field=models.CharField(blank=True, editable=False, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='nodes_model',
            name='machine',
            field=models.CharField(blank=True, editable=False, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='nodes_model',
            name='sub_location',
            field=models.CharField(blank=True, editable=False, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='nodes_model',
            name='tempreture_high',
            field=models.CharField(blank=True, editable=False, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='nodes_model',
            name='tempreture_low',
            field=models.CharField(blank=True, editable=False, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='nodes_model',
            name='time',
            field=models.CharField(blank=True, editable=False, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='nodes_model',
            name='updated_at',
            field=models.CharField(blank=True, editable=False, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='nodes_model',
            name='uuid',
            field=models.CharField(blank=True, editable=False, max_length=300, null=True),
        ),
    ]
