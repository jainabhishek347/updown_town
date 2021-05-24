from django.contrib import admin

# Register your models here.
from profiles.models import Profile
#admin.site.register(Profile)

from django.contrib.gis.admin import OSMGeoAdmin
from .models import Profile

@admin.register(Profile)
class ShopAdmin(OSMGeoAdmin):
    list_display = ('full_name', 'location')