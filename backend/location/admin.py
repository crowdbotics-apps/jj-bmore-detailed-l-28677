from django.contrib import admin
from .models import MapLocation, CustomerLocation, TaskerLocation, TaskLocation

admin.site.register(MapLocation)
admin.site.register(CustomerLocation)
admin.site.register(TaskLocation)
admin.site.register(TaskerLocation)

# Register your models here.
