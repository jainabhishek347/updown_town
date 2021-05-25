from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Profile, ProfileMatch

admin.site.register(ProfileMatch)

@admin.register(Profile)
class ProfileAdmin(OSMGeoAdmin):
    list_display = ('full_name', 'gender', 'email', 'location', 'profile_photo')


