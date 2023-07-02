from rest_framework import serializers
from .models import *


class NodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = nodes_model
        # fields = ('id', 'machine', 'location', 'sub_location', 'humidity','tempreture','tempreture_low','tempreture_high','battery','user_name','delete_status','uuid','_uuid',"humidity_low","humidity_high","CO2_high","CO2_low","CO2",'updated_at','email')
        fields = '__all__' 





class voltageSerializer(serializers.ModelSerializer):
    class Meta:
        model = voltage_parameters
        fields = '__all__' 

class currentSerializer(serializers.ModelSerializer):
    class Meta:
        model = current_parameters
        fields = '__all__' 

class powerSerializer(serializers.ModelSerializer):
    class Meta:
        model = power_parameters
        fields = '__all__' 

class generator_speedSerializer(serializers.ModelSerializer):
    class Meta:
        model = generator_speed_parameters
        fields = '__all__' 

class windspeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = windspeed_parameters
        fields = '__all__' 