# Generated by Django 4.1.5 on 2023-03-18 12:58

from django.db import migrations
import encrypted_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('node', '0033_alter_post_nodes_co2_alter_post_nodes_battery_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post_nodes',
            name='_date',
            field=encrypted_fields.fields.SearchField(blank=True, db_index=True, encrypted_field_name='date', hash_key='8222a7fd4b33e333fd5cfcd2b2c03473515a397855ded9b674bb2779110d8736', max_length=66, null=True),
        ),
        migrations.AddField(
            model_name='post_nodes',
            name='_time',
            field=encrypted_fields.fields.SearchField(blank=True, db_index=True, encrypted_field_name='time', hash_key='8222a7fd4b33e333fd5cfcd2b2c03473515a397855ded9b674bb2779110d8736', max_length=66, null=True),
        ),
        migrations.AddField(
            model_name='post_nodes',
            name='_uuid',
            field=encrypted_fields.fields.SearchField(blank=True, db_index=True, encrypted_field_name='uuid', hash_key='8222a7fd4b33e333fd5cfcd2b2c03473515a397855ded9b674bb2779110d8736', max_length=66, null=True),
        ),
    ]
