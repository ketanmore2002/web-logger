from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
# Register your models here.







@admin.register(nodes_model)
class PersonAdmin(ImportExportModelAdmin):
    pass


# admin.site.register(voltage_temp)
# admin.site.register(current_temp)
# admin.site.register(power_temp)
# admin.site.register(generator_speed_temp)
# admin.site.register(windspeed_temp)

# admin.site.register(voltage_parameters)
# admin.site.register(current_parameters)
# admin.site.register(power_parameters)
# admin.site.register(generator_speed_parameters)
# admin.site.register(windspeed_parameters)
# admin.site.register(battery_parameters)
# admin.site.register(node_health)

# admin.site.register(current_model)

admin.site.register(task)


@admin.register(voltage_model)
class PersonAdmin(ImportExportModelAdmin):
    pass

@admin.register(current_model)
class PersonAdmin(ImportExportModelAdmin):
    pass

@admin.register(power_model)
class PersonAdmin(ImportExportModelAdmin):
    pass

@admin.register(generator_speed_model)
class PersonAdmin(ImportExportModelAdmin):
    pass

@admin.register(windspeed_model)
class PersonAdmin(ImportExportModelAdmin):
    pass




from django.contrib import admin
# Need to import this since auth models get registered on import.
import django.contrib.auth.admin
import django.contrib.auth.models
from django.contrib import auth

# admin.site.unregister(auth.models.User)
# admin.site.unregister(auth.models.Group)