from django.db import models

from encrypted_fields import fields


# Create your models here.


class nodes_model(models.Model):
    machine = fields.EncryptedCharField(max_length=300,blank=True,null=True) 
    location = fields.EncryptedCharField(max_length=300,blank=True,null=True) 
    sub_location = fields.EncryptedCharField(max_length=300,blank=True,null=True)
    battery = fields.EncryptedCharField(max_length=300,blank=True,null=True)
    user_name = models.CharField(max_length=300,blank=True,null=True)
    _delete_status = models.CharField(max_length=300,blank=True,null=True,default="Restore")
    # _delete_status = fields.SearchField(hash_key="8222a7fd4b33e333fd5cfcd2b2c03473515a397855ded9b674bb2779110d8736", encrypted_field_name="delete_status", blank=True,null=True)
    uuid =  fields.EncryptedCharField(max_length=300,blank=True,null=True)
    _uuid = fields.SearchField(hash_key="8222a7fd4b33e333fd5cfcd2b2c03473515a397855ded9b674bb2779110d8736", encrypted_field_name="uuid",blank=True,null=True)
    time = fields.EncryptedCharField(max_length=300,blank=True,null=True)
    date = fields.EncryptedCharField(max_length=300,blank=True,null=True)
    email = fields.EncryptedCharField(max_length=300,blank=True,null=True)
    activate = fields.EncryptedCharField(max_length=300,blank=True,null=True ,default = "False")
    


class voltage_model(models.Model):
    uuid =  models.CharField(max_length=300,blank=True,null=True)
    voltage = models.CharField(max_length=300,blank=True,null=True)
    # voltage_low = models.CharField(max_length=300,blank=True,null=True)
    # voltage_high = models.CharField(max_length=300,blank=True,null=True)
    date = models.DateField(auto_now=True,blank=True,null=True)
    time = models.TimeField(auto_now=True,blank=True,null=True)
class current_model(models.Model):
    uuid =  models.CharField(max_length=300,blank=True,null=True)
    current = models.CharField(max_length=300,blank=True,null=True)
    # current_low = models.CharField(max_length=300,blank=True,null=True)
    # current_high = models.CharField(max_length=300,blank=True,null=True)
    date = models.DateField(auto_now=True,blank=True,null=True)
    time = models.TimeField(auto_now=True,blank=True,null=True)
class power_model(models.Model):
    uuid =  models.CharField(max_length=300,blank=True,null=True)
    power = models.CharField(max_length=300,blank=True,null=True)
    # power_high = models.CharField(max_length=300,blank=True,null=True)
    # power_low = models.CharField(max_length=300,blank=True,null=True)
    date = models.DateField(auto_now=True,blank=True,null=True)
    time = models.TimeField(auto_now=True,blank=True,null=True)
class generator_speed_model(models.Model):
    uuid =  models.CharField(max_length=300,blank=True,null=True)
    generator_speed = models.CharField(max_length=300,blank=True,null=True)
    # generator_speed_high = models.CharField(max_length=300,blank=True,null=True)
    # generator_speed_low = models.CharField(max_length=300,blank=True,null=True)
    date = models.DateField(auto_now=True,blank=True,null=True)
    time = models.TimeField(auto_now=True,blank=True,null=True)
class windspeed_model(models.Model):
    uuid =  models.CharField(max_length=300,blank=True,null=True)
    windspeed =  models.CharField(max_length=300,blank=True,null=True)
    # windspeed_high = models.CharField(max_length=300,blank=True,null=True)
    # windspeed_low = models.CharField(max_length=300,blank=True,null=True)
    date = models.DateField(auto_now=True,blank=True,null=True)
    time = models.TimeField(auto_now=True,blank=True,null=True)

         



class voltage_temp(models.Model):
    uuid =  models.CharField(max_length=300,blank=True,null=True)
    voltage = models.CharField(max_length=300,blank=True,null=True)
    date = models.DateField(auto_now=True,blank=True,null=True)
    time = models.TimeField(auto_now=True,blank=True,null=True)
class current_temp(models.Model):
    uuid =  models.CharField(max_length=300,blank=True,null=True)
    current = models.CharField(max_length=300,blank=True,null=True)
    date = models.DateField(auto_now=True,blank=True,null=True)
    time = models.TimeField(auto_now=True,blank=True,null=True)
class power_temp(models.Model):
    uuid =  models.CharField(max_length=300,blank=True,null=True)
    power = models.CharField(max_length=300,blank=True,null=True)
    date = models.DateField(auto_now=True,blank=True,null=True)
    time = models.TimeField(auto_now=True,blank=True,null=True)
class generator_speed_temp(models.Model):
    uuid =  models.CharField(max_length=300,blank=True,null=True)
    generator_speed = models.CharField(max_length=300,blank=True,null=True)
    date = models.DateField(auto_now=True,blank=True,null=True)
    time = models.TimeField(auto_now=True,blank=True,null=True)
class windspeed_temp(models.Model):
    uuid =  models.CharField(max_length=300,blank=True,null=True)
    windspeed =  models.CharField(max_length=300,blank=True,null=True)
    date = models.DateField(auto_now=True,blank=True,null=True)
    time = models.TimeField(auto_now=True,blank=True,null=True)
   



class voltage_parameters(models.Model):
    uuid =  models.CharField(max_length=300,blank=True,null=True)
    voltage_low = models.CharField(max_length=300,blank=True,null=True)
    voltage_high = models.CharField(max_length=300,blank=True,null=True)
class current_parameters(models.Model):
    uuid =  models.CharField(max_length=300,blank=True,null=True)
    current_low = models.CharField(max_length=300,blank=True,null=True)
    current_high = models.CharField(max_length=300,blank=True,null=True)
class power_parameters(models.Model):
    uuid =  models.CharField(max_length=300,blank=True,null=True)
    power_high = models.CharField(max_length=300,blank=True,null=True)
    power_low = models.CharField(max_length=300,blank=True,null=True)
class generator_speed_parameters(models.Model):
    uuid =  models.CharField(max_length=300,blank=True,null=True)
    generator_speed_high = models.CharField(max_length=300,blank=True,null=True)
    generator_speed_low = models.CharField(max_length=300,blank=True,null=True)
class windspeed_parameters(models.Model):
    uuid =  models.CharField(max_length=300,blank=True,null=True)
    windspeed_high = models.CharField(max_length=300,blank=True,null=True)
    windspeed_low = models.CharField(max_length=300,blank=True,null=True)




class node_health(models.Model):
    uuid =  models.CharField(max_length=300,blank=True,null=True)
    health = models.CharField(max_length=300,blank=True,null=True)
    date = models.DateField(auto_now=True,blank=True,null=True)
    time = models.TimeField(auto_now=True,blank=True,null=True)
    

class time_stamp(models.Model):
    uuid =  models.CharField(max_length=300,blank=True,null=True)
    # parameter = models.CharField(max_length=300,blank=True,null=True)
    date_time = models.DateTimeField(auto_now=True)
    date = models.DateField(auto_now=True,blank=True,null=True)
    time = models.TimeField(auto_now=True,blank=True,null=True)





class battery_parameters(models.Model):
    uuid =  models.CharField(max_length=300,blank=True,null=True)
    battery = models.CharField(max_length=300,blank=True,null=True)


class deleted_nodes(models.Model):
    uuid = models.CharField(max_length=300,blank=True,null=True)
    node_id = models.CharField(max_length=300,blank=True,null=True)
    user_name = models.CharField(max_length=300,blank=True,null=True)
    time = models.TimeField(auto_now_add=True,blank=True,null=True)
    date = models.DateField(auto_now_add=True,blank=True,null=True)
