from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from node import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("",views.index,name='index'),
    # path("data",views.data,name='data'),
    path("get_data_nodes",views.get_data_nodes.as_view(),name='get_data_nodes'),
    path("post_data_nodes",views.post_data_nodes_1.as_view(),name='post_data_nodes'),
    path("delete_data_nodes/<str:id>/",views.delete_data_nodes.as_view(),name='delete_data_nodes'),
    path("update_single_node/<int:pk>/",views.update_single_node.as_view(),name='update_single_node'),

    path("get_single_node/<str:uuid>",views.get_single_node_data.as_view(),name='get_single_node'),

    path("admin_panel",views.admin_panel,name='admin_panel'),
    path("test",views.test,name='test'),
    path("create_node/",views.create_node,name='create_node'),
    path("send_node_data/<str:uid>/<str:user_name>/",views.send_node_data,name='send_node_data'),
    path("graph/",views.graph.as_view(),name='graph'),
    path("logout/", views.logout_view, name="logout"),
    path('generateinvoice/', views.GenerateInvoice.as_view(), name = 'generateinvoice'),
    path('generateinvoice/<str:uuid>/<str:start_time>/<str:end_time>/<str:start_date>/<str:end_date>/', views.GenerateInvoice.as_view(), name = 'generateinvoice'),
    path('publish', views.publish_message, name='publish'),
    path("user_veiw",views.user_veiw.as_view(),name='user_veiw'),
    path("insight_current_week/<str:uid>",views.insight_current_week.as_view(),name='insight_current_week'),
    path("insight_current_month/<str:uid>",views.insight_current_month.as_view(),name='insight_current_month'),
    path("insight_current_range",views.insight_current_range.as_view(),name='insight_current_range'),
    path("glance/",views.glance,name='glance'),
    path("statis/",views.statis.as_view(),name='statis'),
    path("version/",views.version,name='version'),
    path("manage_deleted_nodes/",views.manage_deleted_node.as_view(),name='version'),

    path("volatge_data/",views.volatge_data.as_view(),name='volatge_data'),
    path("current_data/",views.current_data.as_view(),name='current_data'),
    path("power_data/",views.power_data.as_view(),name='power_data'),
    path("generator_speed_data/",views.generator_speed_data.as_view(),name='generator_speed_data'),
    path("windspeed_data/",views.windspeed_data.as_view(),name='windspeed_data'),
    path("battery_data/",views.battery_data.as_view(),name='battery_data'),
    path("node_health_data/",views.health_data.as_view(),name='node_healthy_data'),
    path("time_data/",views.time_data.as_view(),name='time_data'),
    path("notification_data/",views.notification_data.as_view(),name='notification_data'),
    path("check_deleted_nodes/",views.check_deleted_nodes.as_view(),name='check_deleted_nodes'),
    path("task_data/",views.task_data.as_view(),name='task_data'),


]



# $.ajax({
#     url: "/graph"+"/",
#     headers: headers_payload,
#     type: "POST",
#     data: JSON.stringify(payload_add),
#     success: function (data, textStatus, jqXHR) {},
#     error: function (jqXHR, textStatus, errorThrown) {
#       alert(errorThrown);
#     }
#     }),



#   $.ajax({
#     url: "/insight_current_week",
#     headers: headers_payload,
#     type: "POST",
#     success: function (data, textStatus, jqXHR) {
#       console.log(data)
#       $("#insights_week").text(data)
#     },
#     error: function (jqXHR, textStatus, errorThrown) {
#       alert(errorThrown);
#     }
#     })
# },