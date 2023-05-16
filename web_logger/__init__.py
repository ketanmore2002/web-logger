import django
django.setup()

from node.views import client
client.loop_start()