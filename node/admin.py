from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
# Register your models here.

# admin.site.register(nodes_model)
# admin.site.register(user_theme)


@admin.register(nodes_model)
class PersonAdmin(ImportExportModelAdmin):
    pass

@admin.register(post_nodes)
class PersonAdmin(ImportExportModelAdmin):
    pass



from django.contrib import admin
# Need to import this since auth models get registered on import.
import django.contrib.auth.admin
import django.contrib.auth.models
from django.contrib import auth

admin.site.unregister(auth.models.User)
admin.site.unregister(auth.models.Group)