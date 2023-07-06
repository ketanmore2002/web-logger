import json
from django.shortcuts import render ,redirect
from .models import *

from django.http import HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from rest_framework.decorators import api_view ,renderer_classes
from rest_framework.response import Response
from rest_framework import serializers
from .serializers import *
from rest_framework import status

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from django.utils.decorators import method_decorator

from django.views.decorators.csrf import csrf_exempt 
from django.contrib.auth.decorators import login_required
from django.core import serializers as ser

from rest_framework.permissions import IsAuthenticated

from django.views import View
from django.views.generic.edit import CreateView
from rest_framework.views import APIView

from django.conf import settings
from django.core.mail import send_mail
from braces.views import GroupRequiredMixin

from django.contrib.auth.models import User
from django.contrib.auth.models import Group
# from django.contrib.auth.models import user_groups
from django.db.models import Avg


# Create your views here.


def index (request):
    # print(nodes_model.objects.all())
    return redirect("/admin_panel")

def data (request):
    return render(request , "data.html")


class get_data_nodes(GroupRequiredMixin,APIView):
    permission_classes = (IsAuthenticated, )
    group_required = ["user","observer","admin","administrator"]
    def post(self, request):
        posts = nodes_model.objects.all()
        serializer = NodeSerializer(posts, many=True)
        return Response(serializer.data)


class get_single_node_data(GroupRequiredMixin,APIView):
    permission_classes = (IsAuthenticated, )
    group_required = ["user","observer","admin","administrator"]
    def get(self,request,uuid):
        print(uuid)
        result = {}

        if voltage_parameters.objects.filter(uuid=uuid).exists() :
            voltage_para = voltage_parameters.objects.filter(uuid=uuid).values()[0]
            result.update(voltage_para)
        else :
            result.update({"voltage_low" : " Not Available" , "voltage_high" : " Not Available"})


        if current_parameters.objects.filter(uuid=uuid).exists() :
            current_para = current_parameters.objects.filter(uuid=uuid).values()[0]
            result.update(current_para)
        else :
            result.update({"current_low" : " Not Available" , "current_high" : " Not Available"})
        
        if power_parameters.objects.filter(uuid=uuid).exists() :
            power_para = power_parameters.objects.filter(uuid=uuid).values()[0]
            result.update(power_para)
        else :
            result.update({"power_low" : " Not Available" , "power_high" : " Not Available"})
        
        if generator_speed_parameters.objects.filter(uuid=uuid).exists() :
            generator_speed_para = generator_speed_parameters.objects.filter(uuid=uuid).values()[0]
            result.update(generator_speed_para)
        else :
            result.update({"generator_speed_low" : " Not Available" , "generator_speed_high" : " Not Available"})

        if windspeed_parameters.objects.filter(uuid=uuid).exists():
            windspeed_para = windspeed_parameters.objects.filter(uuid=uuid).values()[0]
            result.update(windspeed_para)
        else :
            result.update({"windspeed_low" : " Not Available" , "windspeed_high" : " Not Available"})

        posts = nodes_model.objects.filter(_uuid=uuid).values()[0]
        result.update(posts)

        json_data = json.dumps(result)
        
        return JsonResponse(json_data, safe=False)

        # posts = nodes_model.objects.filter(id=pk)
        # serializer = NodeSerializer(posts, many=True)
        # return Response(serializer.data)


class post_data_nodes_1(GroupRequiredMixin,APIView):
    permission_classes = (IsAuthenticated, )
    group_required = ["user","admin","administrator"]
    def get(self, request):
        snippets = nodes_model.objects.all()
        serializer = NodeSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request):

        dict_data=request.data

        if nodes_model.objects.filter(_uuid = dict_data["uuid"]).exists() :
            return HttpResponse("uuid already exists" ,status=403)
        else :
        
            if  dict_data["voltage_low"] != "undefined" and dict_data["voltage_high"] != "undefined" :
                voltage_parameters.objects.create(uuid = dict_data["uuid"] , voltage_low = dict_data["voltage_low"] , voltage_high = dict_data["voltage_high"])

            if  dict_data["current_low"] != "undefined" and dict_data["current_high"] != "undefined" :
                current_parameters.objects.create(uuid = dict_data["uuid"] , current_low = dict_data["current_low"] , current_high = dict_data["current_high"])

            if  dict_data["power_low"] != "undefined" and dict_data["power_high"] != "undefined" :
                power_parameters.objects.create(uuid = dict_data["uuid"] , power_low = dict_data["power_low"] , power_high = dict_data["power_high"])
            
            if  dict_data["generator_speed_low"] != "undefined" and dict_data["generator_speed_high"] != "undefined" :
                generator_speed_parameters.objects.create(uuid = dict_data["uuid"] , generator_speed_low = dict_data["generator_speed_low"] , generator_speed_high = dict_data["generator_speed_high"])

            if  dict_data["windspeed_low"] != "undefined" and dict_data["windspeed_high"] != "undefined" :
                windspeed_parameters.objects.create(uuid = dict_data["uuid"] , windspeed_low = dict_data["windspeed_low"] , windspeed_high = dict_data["windspeed_high"])

            node = nodes_model.objects.create(machine=dict_data["machine"] , location = dict_data["location"] , sub_location = dict_data["sub_location"] , user_name=dict_data["user_name"], _uuid=dict_data["uuid"] , email=dict_data["email"] )
            
            return Response(status=status.HTTP_201_CREATED)
        # return redirect ("/")




def post_data_nodes(request):


        if request.method == "POST":

            dict_data= request.POST

            # (request.POST['voltage_low'])
        
            if  dict_data["voltage_low"] != "undefined" and dict_data["voltage_high"] != "undefined" :
                voltage_parameters.objects.create(uuid = dict_data["uuid"] , voltage_low = dict_data["voltage_low"] , voltage_high = dict_data["voltage_high"])

            if  dict_data["current_low"] != "undefined" and dict_data["current_high"] != "undefined" :
                current_parameters.objects.create(uuid = dict_data["uuid"] , current_low = dict_data["current_low"] , current_high = dict_data["current_high"])

            if  dict_data["power_low"] != "undefined" and dict_data["power_high"] != "undefined" :
                power_parameters.objects.create(uuid = dict_data["uuid"] , power_low = dict_data["power_low"] , power_high = dict_data["power_high"])
            
            if  dict_data["generator_speed_low"] != "undefined" and dict_data["generator_speed_high"] != "undefined" :
                generator_speed_parameters.objects.create(uuid = dict_data["uuid"] , generator_speed_low = dict_data["generator_speed_low"] , generator_speed_high = dict_data["generator_speed_high"])

            if  dict_data["windspeed_low"] != "undefined" and dict_data["windspeed_high"] != "undefined" :
                windspeed_parameters.objects.create(uuid = dict_data["uuid"] , windspeed_low = dict_data["windspeed_low"] , windspeed_high = dict_data["windspeed_high"])

            node = nodes_model.objects.create(machine=dict_data["machine"] , location =dict_data["location"], sub_location = dict_data["sub_location"] , _user_name= request.user.username, _uuid=dict_data["uuid"] , email=dict_data["email"] )
            
            # return Response(status=status.HTTP_201_CREATED)
            return redirect ("/")


        
        
class user_veiw(GroupRequiredMixin,APIView):
    permission_classes = (IsAuthenticated, )
    group_required = ["user","admin","administrator"]
    def post(self, request):
        dict_data = json.loads(request.body.decode('UTF-8'))
        print(dict_data)
        data = User.objects.create_user(first_name = dict_data["first_name"] , last_name = dict_data["last_name"] , username=dict_data["username"] , password = dict_data["password"] ,is_staff = True)
        my_group = Group.objects.get(name= dict_data["role"]) 
        my_group.user_set.add(data)
        id = data.id
        return HttpResponse(id)
    def delete(self, request):
        dict_data = json.loads(request.body.decode('UTF-8'))
        dict_data = dict_data["id"]
        User.objects.filter(id=dict_data).delete()
        return HttpResponse("User Deleted")
    def put (self,request):
        dict_data = json.loads(request.body.decode('UTF-8'))
        role = dict_data["role"]
        id = dict_data["id"]
        user = User.objects.get(id=id)
        try:
            user.groups.clear()
        except:
            pass
        my_group = Group.objects.get(name= role) 
        my_group.user_set.add(user)
        return HttpResponse("role updated !")

from django.core.cache import cache
class manage_deleted_node(GroupRequiredMixin,APIView):
    permission_classes = (IsAuthenticated, )
    group_required = ["administrator" , "admin" , "user"]
    def post(self, request):
        nodes_model.objects.filter(id = request.data["node_id"]).update(user_name = request.data["user_name"] , _delete_status = "Restore")
        deleted_nodes.objects.filter(node_id = request.data["node_id"]).delete()
        # task.objects.create(status="incomplete")
        cache.set("node", "incomplete",timeout=3)

        return HttpResponse("Done !")
    
    def delete (self , request) :
        uuid = nodes_model.objects.filter(id = request.data["node_id"])[0]
        nodes_model.objects.filter(id = request.data["node_id"]).delete()
        deleted_nodes.objects.filter(node_id = request.data["node_id"]).delete()

        voltage_parameters.objects.filter(uuid=uuid.uuid).delete()
        current_parameters.objects.filter(uuid=uuid.uuid).delete()
        power_parameters.objects.filter(uuid=uuid.uuid).delete()
        generator_speed_parameters.objects.filter(uuid=uuid.uuid).delete()
        windspeed_parameters.objects.filter(uuid=uuid.uuid).delete()

        voltage_temp.objects.filter(uuid=uuid.uuid).delete()
        current_temp.objects.filter(uuid=uuid.uuid).delete()
        power_temp.objects.filter(uuid=uuid.uuid).delete()
        generator_speed_temp.objects.filter(uuid=uuid.uuid).delete()
        windspeed_temp.objects.filter(uuid=uuid.uuid).delete()

        voltage_model.objects.filter(uuid=uuid.uuid).delete()
        current_model.objects.filter(uuid=uuid.uuid).delete()
        power_model.objects.filter(uuid=uuid.uuid).delete()
        generator_speed_model.objects.filter(uuid=uuid.uuid).delete()
        windspeed_model.objects.filter(uuid=uuid.uuid).delete()

        battery_parameters.objects.filter(uuid=uuid.uuid).delete()
        node_health.objects.filter(uuid=uuid.uuid).delete()

        # task.objects.create(status="incomplete")
        cache.set("node", "incomplete",timeout=7)

        return HttpResponse("Done !")



class delete_data_nodes(GroupRequiredMixin,APIView):
   permission_classes = (IsAuthenticated, )
   group_required = ["user","admin","administrator"]
   def post(self, request,id):
        nodes_model.objects.filter(id=id).update(_delete_status = "deleted")
        data = nodes_model.objects.filter(id = id)[0]
        deleted_nodes.objects.create(uuid = data.uuid , node_id = id , user_name = data.user_name)
        return HttpResponse("Done !")
        

@staff_member_required
def admin_panel (request) :

    current = current_temp.objects.all()
    voltage = voltage_temp.objects.all()
    power = power_temp.objects.all()
    generator_speed = generator_speed_temp.objects.all()
    windspeed = windspeed_temp.objects.all()

    current_para = current_parameters.objects.all()
    voltage_para = voltage_parameters.objects.all()
    power_para = power_parameters.objects.all()
    generator_speed_para = generator_speed_parameters.objects.all()
    windspeed_para = windspeed_parameters.objects.all()

    if request.user.groups.filter(name='admin').exists() or request.user.groups.filter(name='administrator').exists():
        data = nodes_model.objects.filter(_delete_status="Restore")
    else:
        data = nodes_model.objects.filter(_delete_status="Restore",user_name = request.user.username)
    users = User.objects.all()
    return render (request,"admin3.html",{"data":data,"users":users ,"voltage" : voltage , "current" : current , "power" : power , "generator_speed" : generator_speed , "windspeed" : windspeed , 
                                          "voltage_para" : voltage_para , "current_para" : current_para , "power_para" : power_para , "generator_speed_para" : generator_speed_para , "windspeed_para" : windspeed_para })
    



class update_single_node (GroupRequiredMixin,APIView):
    permission_classes = (IsAuthenticated, )
    group_required = ["user","admin","administrator"]
    def put(self, request, pk):

        dict_data = request.data
        print(dict_data)

        if  dict_data["voltage_low_value"] == "present" and dict_data["voltage_high_value"] == "present":
            if voltage_parameters.objects.filter(uuid = dict_data["uuid"]).exists() :
                voltage_parameters.objects.filter(uuid = dict_data["uuid"]).update(voltage_low = float(dict_data["voltage_low"]) ,voltage_high = float(dict_data["voltage_high"]))
            else :
                voltage_parameters.objects.create(uuid = dict_data["uuid"] , voltage_low = dict_data["voltage_low"] , voltage_high = dict_data["voltage_high"])
        elif dict_data["voltage_low_value"] == "absent" and dict_data["voltage_high_value"] == "absent":
            voltage_parameters.objects.filter(uuid = dict_data["uuid"]).delete()
            voltage_model.objects.filter(uuid = dict_data["uuid"]).delete()
            voltage_temp.objects.filter(uuid = dict_data["uuid"]).delete()

        
        if  dict_data["current_low_value"] == "present" and dict_data["current_high_value"] == "present":
            if current_parameters.objects.filter(uuid = dict_data["uuid"]).exists() :
                current_parameters.objects.filter(uuid = dict_data["uuid"]).update(current_low = float(dict_data["current_low"]) ,current_high = float(dict_data["current_high"]))
            else :
                current_parameters.objects.create(uuid = dict_data["uuid"] , current_low = dict_data["current_low"] , current_high = dict_data["current_high"])
        elif dict_data["current_low_value"] == "absent" and dict_data["current_high_value"] == "absent":
            current_parameters.objects.filter(uuid = dict_data["uuid"]).delete()
            current_model.objects.filter(uuid = dict_data["uuid"]).delete()
            current_temp.objects.filter(uuid = dict_data["uuid"]).delete()

        
        if  dict_data["power_low_value"] == "present" and dict_data["power_high_value"] == "present":
            if power_parameters.objects.filter(uuid = dict_data["uuid"]).exists() :
                power_parameters.objects.filter(uuid = dict_data["uuid"]).update(power_low = float(dict_data["power_low"]) ,power_high = float(dict_data["power_high"]))
            else :
                power_parameters.objects.create(uuid = dict_data["uuid"] , power_low = dict_data["power_low"] , power_high = dict_data["power_high"])
        elif dict_data["power_low_value"] == "absent" and dict_data["power_high_value"] == "absent":
            power_parameters.objects.filter(uuid = dict_data["uuid"]).delete()
            power_model.objects.filter(uuid = dict_data["uuid"]).delete()
            power_temp.objects.filter(uuid = dict_data["uuid"]).delete()

        
        if  dict_data["generator_speed_low_value"] == "present" and dict_data["generator_speed_high_value"] == "present":
            if generator_speed_parameters.objects.filter(uuid = dict_data["uuid"]).exists() :
                generator_speed_parameters.objects.filter(uuid = dict_data["uuid"]).update(generator_speed_low = float(dict_data["generator_speed_low"]) ,generator_speed_high = float(dict_data["generator_speed_high"]))
            else :
                generator_speed_parameters.objects.create(uuid = dict_data["uuid"] , generator_speed_low = dict_data["generator_speed_low"] , generator_speed_high = dict_data["generator_speed_high"])
        elif dict_data["generator_speed_low_value"] == "absent" and dict_data["generator_speed_high_value"] == "absent":
            generator_speed_parameters.objects.filter(uuid = dict_data["uuid"]).delete()
            generator_speed_model.objects.filter(uuid = dict_data["uuid"]).delete()
            generator_speed_temp.objects.filter(uuid = dict_data["uuid"]).delete()
        

        if  dict_data["windspeed_low_value"] == "present" and dict_data["windspeed_high_value"] == "present":
            if windspeed_parameters.objects.filter(uuid = dict_data["uuid"]).exists() :
                windspeed_parameters.objects.filter(uuid = dict_data["uuid"]).update(windspeed_low = float(dict_data["windspeed_low"]) ,windspeed_high = float(dict_data["windspeed_high"]))
            else :
                windspeed_parameters.objects.create(uuid = dict_data["uuid"] , windspeed_low = dict_data["windspeed_low"] , windspeed_high = dict_data["windspeed_high"])
        elif dict_data["windspeed_low_value"] == "absent" and dict_data["windspeed_high_value"] == "absent":
            windspeed_parameters.objects.filter(uuid = dict_data["uuid"]).delete()
            windspeed_model.objects.filter(uuid = dict_data["uuid"]).delete()
            windspeed_temp.objects.filter(uuid = dict_data["uuid"]).delete()


        node = nodes_model.objects.filter(_uuid=dict_data["uuid"]).update(machine=dict_data["machine"] , location =dict_data["location"], sub_location = dict_data["sub_location"] , user_name= request.user.username, _uuid=dict_data["uuid"] , email=dict_data["email"] )
        return HttpResponse("done")
    



def test (request) :
    return render (request,"test.html")

@staff_member_required
def send_node_data(request,uid,user_name):
    data = nodes_model.objects.filter(_uuid=uid,_user_name=user_name)

    processed_query_voltage = {}
    voltages = voltage_model.objects.filter(uuid=uid)
    for uuid , voltage in voltages :
        if uuid not in processed_query_voltage:
            processed_query_voltage[uuid] = voltage

    processed_query_current = {}
    currents = current_model.objects.filter(uuid=uid)
    for uuid , current in currents :
        if uuid not in processed_query_current:
            processed_query_current[uuid] = current

    processed_query_power = {}
    powers = power_model.objects.filter(_uid=uid).last()
    for uuid , power in powers :
        if uuid not in processed_query_power:
            processed_query_power[uuid] = power

    
    generator_speed = generator_speed_model.objects.filter(uuid=uid).last()
    windspeed = windspeed_model.objects.filter(uuid=uid).last()

    qs_json = ser.serialize('json', data)
    return HttpResponse(qs_json, content_type='application/json')



class volatge_data(GroupRequiredMixin,APIView):
    permission_classes = (IsAuthenticated, )
    group_required = ["user","observer","admin","administrator"]
    def get(self, request):
        data = voltage_temp.objects.all()
        qs_json = ser.serialize('json', data)
        return HttpResponse(qs_json, content_type='application/json')

class current_data(GroupRequiredMixin,APIView):
    permission_classes = (IsAuthenticated, )
    group_required = ["user","observer","admin","administrator"]
    def get(self, request):
        data = current_temp.objects.all()
        qs_json = ser.serialize('json', data)
        return HttpResponse(qs_json, content_type='application/json')

class power_data(GroupRequiredMixin,APIView):
    permission_classes = (IsAuthenticated, )
    group_required = ["user","observer","admin","administrator"]
    def get(self, request):
        data = power_temp.objects.all()
        qs_json = ser.serialize('json', data)
        return HttpResponse(qs_json, content_type='application/json')
    
class generator_speed_data(GroupRequiredMixin,APIView):
    permission_classes = (IsAuthenticated, )
    group_required = ["user","observer","admin","administrator"]
    def get(self, request):
        data = generator_speed_temp.objects.all()
        qs_json = ser.serialize('json', data)
        return HttpResponse(qs_json, content_type='application/json')
    
class windspeed_data(GroupRequiredMixin,APIView):
    permission_classes = (IsAuthenticated, )
    group_required = ["user","observer","admin","administrator"]
    def get(self, request):
        data = windspeed_temp.objects.all()
        qs_json = ser.serialize('json', data)
        return HttpResponse(qs_json, content_type='application/json')
    
class battery_data(GroupRequiredMixin,APIView):
    permission_classes = (IsAuthenticated, )
    group_required = ["user","observer","admin","administrator"]
    def get(self, request):
        data = battery_parameters.objects.all()
        qs_json = ser.serialize('json', data)
        return HttpResponse(qs_json, content_type='application/json')


class health_data(GroupRequiredMixin,APIView):
    permission_classes = (IsAuthenticated, )
    group_required = ["user","observer","admin","administrator"]
    def get(self, request):
        data = node_health.objects.all()
        qs_json = ser.serialize('json', data)
        return HttpResponse(qs_json, content_type='application/json')

class time_data(GroupRequiredMixin,APIView):
    permission_classes = (IsAuthenticated, )
    group_required = ["user","observer","admin","administrator"]
    def get(self, request):
        data = nodes_model.objects.all()
        qs_json = ser.serialize('json', data)
        return HttpResponse(qs_json, content_type='application/json')
    

class notification_data(GroupRequiredMixin,APIView):
    permission_classes = (IsAuthenticated, )
    group_required = ["user","observer","admin","administrator"]
    def get(self, request):
        data = deleted_nodes.objects.all()
        qs_json = ser.serialize('json', data)
        return HttpResponse(qs_json, content_type='application/json')
    


class check_deleted_nodes(GroupRequiredMixin,APIView):
    permission_classes = (IsAuthenticated, )
    group_required = ["user","observer","admin","administrator"]
    def get(self, request):
        data = nodes_model.objects.filter(_delete_status="deleted")
        qs_json = ser.serialize('json', data)
        return HttpResponse(qs_json, content_type='application/json')

# class task_data(GroupRequiredMixin,APIView):
#     permission_classes = (IsAuthenticated, )
#     group_required = ["user","observer","admin","administrator"]
#     def get(self, request):
#         if task.objects.filter(status="incomplete").exists():
#             # data = task.objects.filter(status="incomplete")
#             # qs_json = ser.serialize('json', data)
#             # return HttpResponse(qs_json, content_type='application/json')
#             task.objects.filter(status="incomplete").update(status="complete")
#             return HttpResponse("incomplete")
#         else:
#             return HttpResponse("complete")


class task_data(GroupRequiredMixin,APIView):
    permission_classes = (IsAuthenticated, )
    group_required = ["user","observer","admin","administrator"]
    def get(self, request):
        if cache.get('node'):
            return HttpResponse("incomplete")
        else:
            return HttpResponse("complete")


from datetime import datetime, timedelta
class graph(GroupRequiredMixin,APIView):
    permission_classes = (IsAuthenticated, )
    group_required = ["user","observer","admin","administrator"]
    def post(self, request):
        x = request.data["start_time"]
        y = request.data["end_time"]

        current = list(current_model.objects.filter(uuid = request.data["uuid"] ,date__range=(request.data["start_date"], request.data["end_date"]),time__range=(x,y)).values_list('current', flat=True))
        
        voltage = list(voltage_model.objects.filter(uuid = request.data["uuid"] ,date__range=(request.data["start_date"], request.data["end_date"]),time__range=(x,y)).values_list('voltage', flat=True))
        
        power = list(power_model.objects.filter(uuid = request.data["uuid"] ,date__range=(request.data["start_date"], request.data["end_date"]),time__range=(x,y)).values_list('power', flat=True))
        
        generator_speed = list(generator_speed_model.objects.filter(uuid = request.data["uuid"] ,date__range=(request.data["start_date"], request.data["end_date"]),time__range=(x,y)).values_list('generator_speed', flat=True))

        windspeed = list(windspeed_model.objects.filter(uuid = request.data["uuid"] ,date__range=(request.data["start_date"], request.data["end_date"]),time__range=(x,y)).values_list('windspeed', flat=True))

        max_length = max(len(lst) for lst in [current, voltage, power, generator_speed, windspeed])

        current = [None] * (max_length - len(current)) + current
        voltage = [None] * (max_length - len(voltage)) + voltage
        power = [None] * (max_length - len(power)) + power
        generator_speed = [None] * (max_length - len(generator_speed)) + generator_speed
        windspeed = [None] * (max_length - len(windspeed)) + windspeed

        if request.data["start_date"] == request.data["end_date"] :
            labels = list(time_stamp.objects.filter(date__range=(request.data["start_date"], request.data["end_date"]) , time__range = (x,y)).values_list('time', flat=True))
        else:
            labels = list(time_stamp.objects.filter(date__range=(request.data["start_date"], request.data["end_date"]) , time__range = (x,y)).values_list('date', flat=True))

        data = {
                    'current': current,
                    'voltage': voltage,
                    'power': power,
                    'generator_speed': generator_speed,
                    'windspeed': windspeed,
                    'labels': labels,
                }
        
        json_data = json.dumps(data ,default=str)

        return HttpResponse(json_data, content_type='application/json')
    



class insight_current_month(GroupRequiredMixin,APIView):
    # permission_classes = (IsAuthenticated, )
    group_required = ["user","observer","admin","administrator"]    
    def post(self, request , uid):
        para1 = datetime.today()
        para2 = datetime.today() - timedelta(days=30)
        print(para1, para2)
        insights = node_health.objects.filter(health="Unhealthy" , uuid = uid ,date__range=(para1, para2)).count()
        return HttpResponse(insights, content_type='application/json')

class insight_current_week(GroupRequiredMixin,APIView):
    # permission_classes = (IsAuthenticated, )
    group_required = ["user","observer","admin","administrator"]    
    def post(self, request ,uid):
        days_list = []
        today = datetime.now().day
        for i in range(1,8) :
            days_list.append(datetime.today() - timedelta(days=i)) 
        print(days_list)
        count1 = node_health.objects.filter(health="Unhealthy" , uuid = uid, date = days_list[0]).count()
        count2 = node_health.objects.filter(health="Unhealthy" , uuid = uid, date = days_list[1]).count()
        count3 = node_health.objects.filter(health="Unhealthy" , uuid = uid, date = days_list[2]).count()
        count4 = node_health.objects.filter(health="Unhealthy" , uuid = uid, date = days_list[3]).count()
        count5 = node_health.objects.filter(health="Unhealthy" , uuid = uid, date = days_list[4]).count()
        count6 = node_health.objects.filter(health="Unhealthy" , uuid = uid, date = days_list[5]).count()
        count7 = node_health.objects.filter(health="Unhealthy" , uuid = uid, date = days_list[6]).count()
        insights = count1 + count2 + count3 + count4 + count5 + count6 + count7 
        return HttpResponse(insights, content_type='application/json')


# import statistics
import numpy as np
class statis(GroupRequiredMixin,APIView):
    group_required = ["user","observer","admin","administrator"]    
    def post(self, request ) :
        dict_data = json.loads(request.body.decode('UTF-8'))

        x = request.data["start_time"]
        y = request.data["end_time"]

        data = {}

        if voltage_model.objects.filter(uuid = dict_data["uuid"]).exists():
            voltage_std = round(np.std(np.array(list(voltage_model.objects.filter(uuid = dict_data["uuid"],date__range=(request.data["start_date"], request.data["end_date"]),time__range=(x,y)).values_list('voltage', flat=True)) , dtype=float)) ,2 )
            data["voltage_std"] = voltage_std
            voltage_var = round(np.var(np.array(list(voltage_model.objects.filter(uuid = dict_data["uuid"],date__range=(request.data["start_date"], request.data["end_date"]),time__range=(x,y)).values_list('voltage', flat=True)) , dtype=float)) ,2 )
            data["voltage_var"] = voltage_var
            voltage_mean = round(np.mean(np.array(list(voltage_model.objects.filter(uuid = dict_data["uuid"],date__range=(request.data["start_date"], request.data["end_date"]),time__range=(x,y)).values_list('voltage', flat=True)) , dtype=float)) ,2 )
            data["voltage_mean"] = voltage_mean

        if current_model.objects.filter(uuid = dict_data["uuid"]).exists():
            current_std = round(np.std(np.array(list(current_model.objects.filter(uuid = dict_data["uuid"],date__range=(request.data["start_date"], request.data["end_date"]),time__range=(x,y)).values_list('current', flat=True)) , dtype=float)) ,2 )
            data["current_std"] = current_std
            current_var = round(np.var(np.array(list(current_model.objects.filter(uuid = dict_data["uuid"],date__range=(request.data["start_date"], request.data["end_date"]),time__range=(x,y)).values_list('current', flat=True)) , dtype=float)) ,2 )
            data["current_var"] = current_var
            current_mean = round(np.mean(np.array(list(current_model.objects.filter(uuid = dict_data["uuid"],date__range=(request.data["start_date"], request.data["end_date"]),time__range=(x,y)).values_list('current', flat=True)) , dtype=float)) ,2 )
            data["current_mean"] = current_mean

            
        if power_model.objects.filter(uuid = dict_data["uuid"]).exists():
            power_std = round(np.std(np.array(list(power_model.objects.filter(uuid = dict_data["uuid"],date__range=(request.data["start_date"], request.data["end_date"]),time__range=(x,y)).values_list('power', flat=True)) , dtype=float)) ,2 )
            data["power_std"] = power_std
            power_var = round(np.var(np.array(list(power_model.objects.filter(uuid = dict_data["uuid"],date__range=(request.data["start_date"], request.data["end_date"]),time__range=(x,y)).values_list('power', flat=True)) , dtype=float)) ,2 )
            data["power_var"] = power_var
            power_mean = round(np.mean(np.array(list(power_model.objects.filter(uuid = dict_data["uuid"],date__range=(request.data["start_date"], request.data["end_date"]),time__range=(x,y)).values_list('power', flat=True)) , dtype=float)) ,2 )
            data["power_mean"] = power_mean
            
        if generator_speed_model.objects.filter(uuid = dict_data["uuid"]).exists():
            generator_speed_std = round(np.std(np.array(list(generator_speed_model.objects.filter(uuid = dict_data["uuid"],date__range=(request.data["start_date"], request.data["end_date"]),time__range=(x,y)).values_list('generator_speed', flat=True)),dtype=float)) ,2 )
            data["generator_speed_std"] = generator_speed_std
            generator_speed_var = round(np.var(np.array(list(generator_speed_model.objects.filter(uuid = dict_data["uuid"],date__range=(request.data["start_date"], request.data["end_date"]),time__range=(x,y)).values_list('generator_speed', flat=True)),dtype=float)) ,2 )
            data["generator_speed_var"] = generator_speed_var
            generator_speed_mean = round(np.mean(np.array(list(generator_speed_model.objects.filter(uuid = dict_data["uuid"],date__range=(request.data["start_date"], request.data["end_date"]),time__range=(x,y)).values_list('generator_speed', flat=True)),dtype=float)) ,2 )
            data["generator_speed_mean"] = generator_speed_mean
            

        if windspeed_model.objects.filter(uuid = dict_data["uuid"]).exists():
            windspeed_std = round(np.std(np.array(list(windspeed_model.objects.filter(uuid = dict_data["uuid"],date__range=(request.data["start_date"], request.data["end_date"]),time__range=(x,y)).values_list('windspeed', flat=True)),dtype=float)) ,2 )
            data["windspeed_std"] = windspeed_std
            windspeed_var = round(np.var(np.array(list(windspeed_model.objects.filter(uuid = dict_data["uuid"],date__range=(request.data["start_date"], request.data["end_date"]),time__range=(x,y)).values_list('windspeed', flat=True)),dtype=float)) ,2 )
            data["windspeed_var"] = windspeed_var
            windspeed_mean = round(np.mean(np.array(list( windspeed_model.objects.filter(uuid = dict_data["uuid"],date__range=(request.data["start_date"], request.data["end_date"]),time__range=(x,y)).values_list('windspeed', flat=True)),dtype=float)) ,2 )
            data["windspeed_mean"] = windspeed_mean

        json_data = json.dumps(data)
        return JsonResponse(json_data , safe = False)
        

        


class insight_current_range(GroupRequiredMixin,APIView):
    # permission_classes = (IsAuthenticated, )
    group_required = ["user","observer","admin","administrator"]    
    def post(self, request ):
        x = request.data["start_time"]
        y = request.data["end_time"]
        # print(request.data["start_date"])
        data = node_health.objects.filter(health="Unhealthy" , uuid = request.data["uuid"] ,date__range=(request.data["start_date"], request.data["end_date"]),time__range=(x,y)).count()
        # qs_json = ser.serialize('json', data)
        return HttpResponse(data, content_type='application/json')



from django.contrib.auth import logout
@login_required(login_url='/')  # redirect when user is not logged in
def logout_view(request):
    logout(request)
    return redirect('/')


from django.template.loader import get_template
from io import BytesIO
from xhtml2pdf import pisa

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)#, link_callback=fetch_resources)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None





class GenerateInvoice(GroupRequiredMixin, APIView):
    group_required = ["user", "observer", "admin", "administrator"]

    def get(self, request, uuid, start_time, end_time, start_date, end_date):

        current_data = current_model.objects.filter(uuid = uuid ,date__range=(start_date, end_date),time__range=(start_time,end_time)).values('current')
        voltage_data = voltage_model.objects.filter(uuid = uuid ,date__range=(start_date, end_date),time__range=(start_time,end_time)).values('voltage')
        generator_speed_data = generator_speed_model.objects.filter(uuid = uuid ,date__range=(start_date, end_date),time__range=(start_time,end_time)).values('generator_speed')
        power_data = power_model.objects.filter(uuid = uuid ,date__range=(start_date, end_date),time__range=(start_time,end_time)).values('power')
        windspeed_data = windspeed_model.objects.filter(uuid = uuid ,date__range=(start_date, end_date),time__range=(start_time,end_time)).values('windspeed')
        time_data = time_stamp.objects.filter(date__range=(start_date, end_date),time__range=(start_time,end_time)).values('time')
        date_data = time_stamp.objects.filter(date__range=(start_date, end_date),time__range=(start_time,end_time)).values('date')

        combined_data = []

        max_length = max(len(current_data), len(voltage_data), len(generator_speed_data), len(power_data), len(windspeed_data))


        for i in range(max_length):
            data = {}
            if current_data:
                data['current'] = current_data[i]['current']
            else:
                data['current'] = "NA"
            if voltage_data:
                data['voltage'] = voltage_data[i]['voltage']
            else:
                data['voltage'] = "NA"
            if generator_speed_data:
                data['generator_speed'] = generator_speed_data[i]['generator_speed']
            else:
                data['generator_speed'] = "NA"
            if power_data:
                data['power'] = power_data[i]['power']
            else:
                data['power'] = "NA"
            if windspeed_data:
                data['windspeed'] = windspeed_data[i]['windspeed']
            else:
                data['windspeed'] = "NA"

            data['time'] = time_data[i]['time']
            data['date'] = date_data[i]['date']
        
            combined_data.append(data)

        return render(request, "tables.html", {"data": combined_data , "uuid" : uuid , "start_time" : start_time , "end_time" : end_time , "start_date" : start_date , "end_date" : end_date})

import paho.mqtt.client as mqtt


def on_connect(mqtt_client, userdata, flags, rc):
   if rc == 0:
       print('Connected successfully')
    #    mqtt_client.subscribe('send_data')
   else:
       print('Bad connection. Code:', rc)

import ast
def on_message(mqtt_client, userdata, msg):
    if msg.topic == "send_data":
        tempx = msg.payload
        dict_str = tempx.decode("UTF-8")
        dict_data = ast.literal_eval(dict_str)
        # print(f'Received message on topic: {msg.topic} with payload: {dict_data}')
        rc, mid = client.publish("django/mqtt",str(dict_data))
        data = post_nodes.objects.create(**dict_data)
        # print("done!")
        nodes_model.objects.filter(_uuid = data.uuid , _user_name=data.user_name).update(current=data.current , voltage = data.voltage , power = data.power , date = data.date , time = data.time , battery = data.battery , lpm = data.lpm)
        node = nodes_model.objects.filter(_uuid = data.uuid , _user_name=data.user_name)[0]
        if int(node.current) > int(node.current_high) or int(node.current) < int(node.current_low) or int(node.power) > int(node.power_high) or int(node.power) < int(node.power_low) or int(node.voltage) > int(node.voltage_high) or int(node.voltage) < int(node.voltage_low) or int(node.lpm) > int(node.lpm_high) or int(node.lpm) < int(node.lpm_low)  :
            data.faulty = "True"
            data.save()
            subject = 'Unhealthy Node'
            message = 'Hi ' + node.user_name +","+node.uuid+ ' is unhealthy please check it '
            email_from = settings.EMAIL_HOST_USER
            recipient_list = (node.email).split(",")
            send_mail( subject, message, email_from, recipient_list )
            return HttpResponse("Saved !")
        else:
            return HttpResponse("500")
    else:
        pass


MQTT_SERVER = 'broker.emqx.io'
MQTT_PORT = 1883
MQTT_KEEPALIVE = 60
MQTT_USER = 'admin'
MQTT_PASSWORD = 'admin'

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(MQTT_USER, MQTT_PASSWORD)
client.connect(
    host=MQTT_SERVER,
    port=MQTT_PORT,
    keepalive=MQTT_KEEPALIVE
)


import json
from django.http import JsonResponse
from paho.mqtt import client as mqtt_client


def publish_message(request):
    request_data = json.loads(request.body)
    # print(request_data)
    rc, mid = client.publish(request_data['topic'], request_data['msg'])
    return JsonResponse({'code': rc})




@csrf_exempt
def create_node(request):
    try :
        if request.method == 'POST':
            dict_data = json.loads(request.body.decode('UTF-8'))
            topic = dict_data.get("topic")
            del dict_data['topic']

            if nodes_model.objects.filter(_uuid = dict_data["uuid"]) :

                status = "healthy"
                try :
                    if voltage_parameters.objects.filter(uuid = dict_data["uuid"]).exists() :
                        voltage_para = voltage_parameters.objects.filter(uuid = dict_data["uuid"])[0]
                        voltage_model.objects.create(uuid = dict_data["uuid"] , voltage = dict_data["voltage"])
                        voltage_temp.objects.filter(uuid = dict_data["uuid"]).delete()
                        voltage_temp.objects.create(uuid = dict_data["uuid"] , voltage = dict_data["voltage"])
                        if float(dict_data["voltage"]) < float(voltage_para.voltage_low ) or float(dict_data["voltage"]) > float(voltage_para.voltage_high ) :
                            status = "unhealthy"
                    else:
                        pass
                except:
                    pass
            

                try:
                    if current_parameters.objects.filter(uuid = dict_data["uuid"]).exists() :
                        current_para = current_parameters.objects.filter(uuid = dict_data["uuid"])[0]
                        current_model.objects.create(uuid = dict_data["uuid"] , current = dict_data["current"])
                        current_temp.objects.filter(uuid = dict_data["uuid"]).delete()
                        current_temp.objects.create(uuid = dict_data["uuid"] , current = dict_data["current"])
                        if float(dict_data["current"]) < float(current_para.current_low ) or float(dict_data["current"]) > float(current_para.current_high ) :
                            status = "unhealthy"
                    else:
                        pass
                except:
                    pass


                try:
                    if power_parameters.objects.filter(uuid = dict_data["uuid"]).exists() and "power" in dict_data.keys() :
                        power_para = power_parameters.objects.filter(uuid = dict_data["uuid"])[0]
                        power_model.objects.create(uuid = dict_data["uuid"] , power = dict_data["power"])
                        power_temp.objects.filter(uuid = dict_data["uuid"]).delete()
                        power_temp.objects.create(uuid = dict_data["uuid"] , power = dict_data["power"])
                        if float(dict_data["power"]) < float(power_para.power_low ) or float(dict_data["power"]) > float(power_para.power_high ) :
                            status = "unhealthy"
                    else:
                        pass
                except:
                    pass


                try:
                    if generator_speed_parameters.objects.filter(uuid = dict_data["uuid"]).exists() and "generator_speed" in dict_data.keys() :
                        generator_speed_para = generator_speed_parameters.objects.filter(uuid = dict_data["uuid"])[0]
                        generator_speed_model.objects.create(uuid = dict_data["uuid"] , generator_speed = dict_data["generator_speed"])
                        generator_speed_temp.objects.filter(uuid = dict_data["uuid"]).delete()
                        generator_speed_temp.objects.create(uuid = dict_data["uuid"] , generator_speed = dict_data["generator_speed"] )
                        if float(dict_data["generator_speed"]) < float(generator_speed_para.generator_speed_low ) or float(dict_data["generator_speed"]) > float(generator_speed_para.generator_speed_high ) :
                            status = "unhealthy"
                    else :
                        pass
                except:
                    pass


                try :
                    if windspeed_parameters.objects.filter(uuid = dict_data["uuid"]).exists() and "windspeed" in dict_data.keys() :
                        windspeed_para = windspeed_parameters.objects.filter(uuid = dict_data["uuid"])[0]
                        windspeed_model.objects.create(uuid = dict_data["uuid"] , windspeed = dict_data["windspeed"])
                        windspeed_temp.objects.filter(uuid = dict_data["uuid"]).delete()
                        windspeed_temp.objects.create(uuid = dict_data["uuid"] , windspeed = dict_data["windspeed"])
                        if float(dict_data["windspeed"]) < float(windspeed_para.windspeed_low ) or float(dict_data["windspeed"]) > float(windspeed_para.windspeed_high ) :
                            status = "unhealthy"
                    else:
                        pass
                except:
                    pass

                battery_parameters.objects.filter(uuid = dict_data["uuid"]).delete()
                battery_parameters.objects.create(uuid = dict_data["uuid"] ,  battery = dict_data["battery"])
                nodes_model.objects.filter(_uuid = dict_data["uuid"]).update(battery = dict_data["battery"])
                time_stamp.objects.create()
                # nodes_model.objects.filter(_uuid = dict_data["uuid"]).update(time = dict_data["time"] , date = dict_data["date"] ,activate = "True")

                if status == "unhealthy" :
                    node_health.objects.filter(uuid = dict_data["uuid"]).delete()
                    node_health.objects.create(uuid = dict_data["uuid"] , health = "Unhealthy")
                    info = nodes_model.objects.filter(_uuid = dict_data["uuid"])[0]
                    subject = 'Unhealthy Node'
                    message = 'Hi ' + info.user_name +","+dict_data["uuid"]+ ' is unhealthy please check it '
                    email_from = settings.EMAIL_HOST_USER
                    recipient_list = (info.email).split(",")
                    send_mail( subject, message, email_from, recipient_list )
                    return HttpResponse("saved" , status = 201)
                else:
                    node_health.objects.filter(uuid = dict_data["uuid"]).delete()
                    node_health.objects.create(uuid = dict_data["uuid"] , health = "Healthy")
                    return HttpResponse("saved" , status = 201)
                
            else:return HttpResponse("Node with uuid does not exists",status=404)

    except:
        return HttpResponse("This error is caused by following reasons : 1) Wrong user name or node uid 2) Blank post request  3) String Values Provide in the json format" , status = 404)


def glance (request):

    current = current_temp.objects.all()
    voltage = voltage_temp.objects.all()
    power = power_temp.objects.all()
    generator_speed = generator_speed_temp.objects.all()
    windspeed = windspeed_temp.objects.all()

    current_para = current_parameters.objects.all()
    voltage_para = voltage_parameters.objects.all()
    power_para = power_parameters.objects.all()
    generator_speed_para = generator_speed_parameters.objects.all()
    windspeed_para = windspeed_parameters.objects.all()

    if request.user.groups.filter(name='admin').exists() or request.user.groups.filter(name='administrator').exists():
        data = nodes_model.objects.filter(_delete_status="Restore")
    else:
        data = nodes_model.objects.filter(_delete_status="Restore",user_name = request.user.username)

    # data = nodes_model.objects.filter(_delete_status="Restore")
    return render (request,"glance.html",{"data":data, "voltage" : voltage , "current" : current , "power" : power , "generator_speed" : generator_speed , "windspeed" : windspeed , 
                                          "voltage_para" : voltage_para , "current_para" : current_para , "power_para" : power_para , "generator_speed_para" : generator_speed_para , "windspeed_para" : windspeed_para })

def version(request) :
    return HttpResponse("current version : 3.0")




# subject = 'Unhealthy Node'
# message = 'Hi ' + node.user_name +","+node.uuid+ ' is unhealthy please check it '
# email_from = settings.EMAIL_HOST_USER
# recipient_list = (node.email).split(",")
# send_mail( subject, message, email_from, recipient_list )