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



# Create your views here.


def index (request):
    # print(nodes_model.objects.all())
    return redirect("/admin_panel")

def data (request):
    return render(request , "data.html")


class get_data_nodes(GroupRequiredMixin,APIView):
    permission_classes = (IsAuthenticated, )
    group_required = ["user","observer","admin","super admins"]
    def post(self, request):
        posts = nodes_model.objects.all()
        serializer = NodeSerializer(posts, many=True)
        return Response(serializer.data)


class get_single_node(GroupRequiredMixin,APIView):
    permission_classes = (IsAuthenticated, )
    group_required = ["user","observer","admin","super admins"]
    def get(self, request,pk):
        posts = nodes_model.objects.filter(id=pk)
        serializer = NodeSerializer(posts, many=True)
        return Response(serializer.data)


class post_data_nodes(GroupRequiredMixin,APIView):
    permission_classes = (IsAuthenticated, )
    group_required = ["user","admin","super admins"]
    def get(self, request):
        snippets = nodes_model.objects.all()
        serializer = NodeSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request):
        node = NodeSerializer(data=request.data)
        if node.is_valid():
            node.save()
            return Response(node.data, status=status.HTTP_201_CREATED)
        return Response(node.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
class user_veiw(GroupRequiredMixin,APIView):
    permission_classes = (IsAuthenticated, )
    group_required = ["user","admin","super admins"]
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


class delete_data_nodes(GroupRequiredMixin,APIView):
   permission_classes = (IsAuthenticated, )
   group_required = ["user","admin","super admins"]
   def post(self, request,id):
        nodes_model.objects.filter(id=id).delete()
        return HttpResponse("Done !")
        

@staff_member_required
def admin_panel (request) :
    if request.user.groups.filter(name='admin').exists() or request.user.groups.filter(name='super admins').exists():
        data = nodes_model.objects.filter(_delete_status="Restore")
    else:
        data = nodes_model.objects.filter(_delete_status="Restore",_user_name = request.user.username)
    users = User.objects.all()
    if user_theme.objects.filter(user_id = request.user.id).exists():
        if (user_theme.objects.filter(user_id = request.user.id)[0]).theme == "theme-1" :
            return render (request,"admin.html",{"data":data,"users":users})
        elif (user_theme.objects.filter(user_id = request.user.id)[0]).theme == "theme-2" :
            return render (request,"admin2.html",{"data":data,"users":users})
        elif (user_theme.objects.filter(user_id = request.user.id)[0]).theme == "theme-3" :
            return render (request,"admin3.html",{"data":data,"users":users})
    else:
        return render (request,"admin.html",{"data":data,"users":users})
    



class update_single_node (GroupRequiredMixin,APIView):
    permission_classes = (IsAuthenticated, )
    group_required = ["user","admin","super admins"]
    def post(self, request,pk):
        x = request.data
        nodes_model.objects.filter(id=pk).update(**x)
        return HttpResponse("updated !")

def test (request) :
    return render (request,"test.html")

@staff_member_required
def send_node_data(request,uid,user_name):
    data = nodes_model.objects.filter(_uuid=uid,_user_name=user_name)
    qs_json = ser.serialize('json', data)
    return HttpResponse(qs_json, content_type='application/json')



class all_data(GroupRequiredMixin,APIView):
    permission_classes = (IsAuthenticated, )
    group_required = ["user","observer","admin","super admins"]
    def get(self, request):
        data = nodes_model.objects.all()
        qs_json = ser.serialize('json', data)
        return HttpResponse(qs_json, content_type='application/json')


import datetime
def convert_dates(dt_str):
    return datetime.datetime.strptime(dt_str, "%d/%m/%Y").strftime("%Y-%m-%d")

from datetime import datetime, timedelta

class graph(GroupRequiredMixin,APIView):
    permission_classes = (IsAuthenticated, )
    group_required = ["user","observer","admin","super admins"]
    def post(self, request):
        x = request.data["start_time"]
        y = request.data["end_time"]
        # print(request.data["start_date"])
        data = post_nodes.objects.filter(uuid = request.data["uuid"] ,date__range=(request.data["start_date"], request.data["end_date"]),time__range=(x,y))
        qs_json = ser.serialize('json', data)

        return HttpResponse(qs_json, content_type='application/json')

class insight_current_month(GroupRequiredMixin,APIView):
    # permission_classes = (IsAuthenticated, )
    group_required = ["user","observer","admin","super admins"]    
    def post(self, request , uid):
        para1 = datetime.today()
        para2 = datetime.today() - timedelta(days=30)
        print(para1, para2)
        insights = post_nodes.objects.filter(faulty="True" , uuid = uid ,date__range=(para1, para2)).count()
        return HttpResponse(insights, content_type='application/json')

class insight_current_week(GroupRequiredMixin,APIView):
    # permission_classes = (IsAuthenticated, )
    group_required = ["user","observer","admin","super admins"]    
    def post(self, request ,uid):
        days_list = []
        today = datetime.now().day
        for i in range(1,8) :
            days_list.append(datetime.today() - timedelta(days=i)) 
        print(days_list)
        count1 = post_nodes.objects.filter(faulty="True" , uuid = uid, date = days_list[0]).count()
        count2 = post_nodes.objects.filter(faulty="True" , uuid = uid, date = days_list[1]).count()
        count3 = post_nodes.objects.filter(faulty="True" , uuid = uid, date = days_list[2]).count()
        count4 = post_nodes.objects.filter(faulty="True" , uuid = uid, date = days_list[3]).count()
        count5 = post_nodes.objects.filter(faulty="True" , uuid = uid, date = days_list[4]).count()
        count6 = post_nodes.objects.filter(faulty="True" , uuid = uid, date = days_list[5]).count()
        count7 = post_nodes.objects.filter(faulty="True" , uuid = uid, date = days_list[6]).count()
        insights = count1 + count2 + count3 + count4 + count5 + count6 + count7 
        return HttpResponse(insights, content_type='application/json')

class insight_current_range(GroupRequiredMixin,APIView):
    # permission_classes = (IsAuthenticated, )
    group_required = ["user","observer","admin","super admins"]    
    def post(self, request ):
        x = request.data["start_time"]
        y = request.data["end_time"]
        # print(request.data["start_date"])
        data = post_nodes.objects.filter(faulty="True" , uuid = request.data["uuid"] ,date__range=(request.data["start_date"], request.data["end_date"]),time__range=(x,y)).count()
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




class GenerateInvoice(GroupRequiredMixin,APIView):
    group_required = ["user","observer","admin","super admins"]    
    def get(self, request,uuid,start_time,end_time,start_date,end_date):
    # def get(self, request):

        # try:
            # start_time = request.data["start_time"]
            # end_time = request.data["end_time"]
            # start_date = request.data["start_date"]
            # end_date = request.data["end_date"]
            # uuid = request.data["uuid"]
            # print(start_time)
            # print(end_time)
            # print(start_date)
            # print(end_date)
            # print(uuid)

            pri = post_nodes.objects.filter(uuid = uuid ,date__range=(start_date, end_date),time__range=(start_time,end_time))
            # pri=post_nodes.objects.all()  #you can filter using order_id as well
        # except:
        #     return HttpResponse("505 Not Found")
            data = {
                'time': start_time+"-"+end_time,
                'date': start_date+"-"+end_date,
                'uuid':uuid,
                'pri':pri
            }
            pdf = render_to_pdf('table.html',data )
            return HttpResponse(pdf, content_type='application/pdf')

            # force download
            # if pdf:
            #     response = HttpResponse(pdf, content_type='application/pdf')
            #     filename = "Invoice_%s.pdf" %(['order_id'])
            #     content = "inline; filename='%s'" %(filename)
            #     #download = request.GET.get("download")
            #     #if download:
            #     content = "attachment; filename=%s" %(filename)
            #     response['Content-Disposition'] = content
            #     return response
            # return HttpResponse("Not found")



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
    if request.method == 'POST':
        dict_data = json.loads(request.body.decode('UTF-8'))
        print(dict_data)
        topic = dict_data.get("topic")
        del dict_data['topic']
        rc, mid = client.publish(topic,str(dict_data))
        data = post_nodes.objects.create(**dict_data)
        nodes_model.objects.filter(_uuid = data.uuid , _user_name=data.user_name).update(current=data.current , voltage = data.voltage , power = data.power , date = data.date , time = data.time , battery = data.battery , energy = data.energy , power_factor = data.power_factor , frequency = data.frequency , windspeed = data.windspeed , shaft_speed = data.shaft_speed , torque = data.torque)
        node = nodes_model.objects.filter(_uuid = data.uuid , _user_name=data.user_name)[0]
        if int(node.current) > int(node.current_high) or int(node.current) < int(node.current_low) or int(node.power) > int(node.power_high) or int(node.power) < int(node.power_low) or int(node.voltage) > int(node.voltage_high) or int(node.voltage) < int(node.voltage_low) :
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


def change_theme (request,id,theme):
    id = request.user.id
    if user_theme.objects.filter(user_id = id).exists():
        user_theme.objects.update(user_id = id , theme = theme)
    else :
        user_theme.objects.create(user_id = id , theme = theme)
    return redirect("/")



def glance (request):
    post_nodes.objects.all().delete()
    data = nodes_model.objects.all()
    return render (request,"glance.html",{"data":data })