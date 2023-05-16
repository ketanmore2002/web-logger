from rest_framework import serializers
from .models import *


class NodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = nodes_model
        # fields = ('id', 'machine', 'location', 'sub_location', 'humidity','tempreture','tempreture_low','tempreture_high','battery','user_name','delete_status','uuid','_uuid',"humidity_low","humidity_high","CO2_high","CO2_low","CO2",'updated_at','email')
        fields = '__all__' 





class PostNodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = post_nodes
        fields = ('id','humidity','tempreture','battery','user_name','uuid',"CO2",'updated_at')
        # fields = '__all__' 