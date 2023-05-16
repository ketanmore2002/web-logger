from django.db import models
import uuid

from encrypted_fields import fields


# Create your models here.

CHOICES = (
    # ("Keep Deleted", "Keep Deleted"),
    ("Restore", "Restore"),
)


def get_hash_key():
    # This must return a suitable string, eg from secrets.token_hex(32)
    return "8222a7fd4b33e333fd5cfcd2b2c03473515a397855ded9b674bb2779110d8736"

class nodes_model(models.Model):
    machine = fields.EncryptedCharField(max_length=300,blank=True,null=True) 
    location = fields.EncryptedCharField(max_length=300,blank=True,null=True) 
    sub_location = fields.EncryptedCharField(max_length=300,blank=True,null=True)

    voltage = fields.EncryptedCharField(max_length=300,blank=True,null=True,editable=False)
    voltage_low = fields.EncryptedCharField(max_length=300,blank=True,null=True)
    voltage_high = fields.EncryptedCharField(max_length=300,blank=True,null=True)

    current = fields.EncryptedCharField(max_length=300,blank=True,null=True,editable=False)
    current_low = fields.EncryptedCharField(max_length=300,blank=True,null=True)
    current_high = fields.EncryptedCharField(max_length=300,blank=True,null=True)

    power = fields.EncryptedCharField(max_length=300,blank=True,null=True,editable=False)
    power_high = fields.EncryptedCharField(max_length=300,blank=True,null=True)
    power_low = fields.EncryptedCharField(max_length=300,blank=True,null=True)

    energy  = fields.EncryptedCharField(max_length=300,blank=True,null=True,editable=False)
    energy_high = fields.EncryptedCharField(max_length=300,blank=True,null=True)
    energy_low = fields.EncryptedCharField(max_length=300,blank=True,null=True)

    power_factor = fields.EncryptedCharField(max_length=300,blank=True,null=True,editable=False)
    power_factor_high = fields.EncryptedCharField(max_length=300,blank=True,null=True)
    power_factor_low = fields.EncryptedCharField(max_length=300,blank=True,null=True)

    frequency = fields.EncryptedCharField(max_length=300,blank=True,null=True,editable=False)
    frequency_high = fields.EncryptedCharField(max_length=300,blank=True,null=True)
    frequency_low = fields.EncryptedCharField(max_length=300,blank=True,null=True)

    windspeed = fields.EncryptedCharField(max_length=300,blank=True,null=True,editable=False)
    windspeed_high = fields.EncryptedCharField(max_length=300,blank=True,null=True)
    windspeed_low = fields.EncryptedCharField(max_length=300,blank=True,null=True)

    shaft_speed = fields.EncryptedCharField(max_length=300,blank=True,null=True,editable=False)
    shaft_speed_high = fields.EncryptedCharField(max_length=300,blank=True,null=True)
    shaft_speed_low = fields.EncryptedCharField(max_length=300,blank=True,null=True)

    torque = fields.EncryptedCharField(max_length=300,blank=True,null=True,editable=False)
    torque_high = fields.EncryptedCharField(max_length=300,blank=True,null=True)
    torque_low = fields.EncryptedCharField(max_length=300,blank=True,null=True)

    battery = fields.EncryptedCharField(max_length=300,blank=True,null=True)
    user_name = fields.EncryptedCharField(max_length=300,blank=True,null=True)
    _user_name = fields.SearchField(hash_key="8222a7fd4b33e333fd5cfcd2b2c03473515a397855ded9b674bb2779110d8736", encrypted_field_name="user_name",blank=True,null=True)
    delete_status = fields.EncryptedCharField(max_length=300,blank=True,null=True,editable=False,default="Restore")
    _delete_status = fields.SearchField(hash_key="8222a7fd4b33e333fd5cfcd2b2c03473515a397855ded9b674bb2779110d8736", encrypted_field_name="delete_status", blank=True,null=True)
    uuid =  fields.EncryptedCharField(max_length=300,blank=True,null=True)
    _uuid = fields.SearchField(hash_key="8222a7fd4b33e333fd5cfcd2b2c03473515a397855ded9b674bb2779110d8736", encrypted_field_name="uuid",blank=True,null=True)
    time = fields.EncryptedCharField(max_length=300,blank=True,null=True)
    date = fields.EncryptedCharField(max_length=300,blank=True,null=True)
    email = fields.EncryptedCharField(max_length=300,blank=True,null=True)
    longitude  = fields.EncryptedCharField(max_length=300,blank=True,null=True)
    latitude  = fields.EncryptedCharField(max_length=300,blank=True,null=True)

         

# {"uid":"PV444","user":"Suchitra","temperature":"-242.02","humidity":"0.00","co2":"0.00","battery":"0"}

class post_nodes(models.Model):
    uuid = models.CharField(max_length=300,blank=True,null=True)
    user_name = models.CharField(max_length=300,blank=True,null=True)
    battery = models.CharField(max_length=300,blank=True,null=True)
    faulty = models.CharField(max_length=300,blank=True,null=True,default="False")
    time = models.TimeField(auto_now_add=True,blank=True,null=True)
    date = models.DateField(auto_now_add=True,blank=True,null=True)
    updated_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    power = models.CharField(max_length=300,blank=True,null=True)
    current = models.CharField(max_length=300,blank=True,null=True)
    voltage = models.CharField(max_length=300,blank=True,null=True)
    energy = models.CharField(max_length=300,blank=True,null=True)
    power_factor = models.CharField(max_length=300,blank=True,null=True)
    frequency = models.CharField(max_length=300,blank=True,null=True)
    windspeed = models.CharField(max_length=300,blank=True,null=True)
    shaft_speed = models.CharField(max_length=300,blank=True,null=True)
    torque = models.CharField(max_length=300,blank=True,null=True)



class user_theme(models.Model):
    user_id = models.CharField(max_length=300,blank=True,null=True)
    theme = models.CharField(max_length=300,blank=True,null=True)
