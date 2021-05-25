from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from profiles.models import Profile, ProfileMatch
from drf_extra_fields.geo_fields import PointField
from math import sin, cos, sqrt, atan2, radians



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class ProfileSerializer(serializers.ModelSerializer):
    profile_photo = serializers.ImageField()
    location = PointField(required=False)
    class Meta:
        model = Profile
        read_only_fields = ('id',)
        fields = ["user","full_name", 'gender' , 'location', 'email', 'profile_photo', 'match']

class ListSerializer(serializers.ModelSerializer):
    profile_photo = serializers.ImageField()
    location = PointField(required=False)
    distance = serializers.SerializerMethodField('calculate_distance')
    def calculate_distance(self,obj):
        obj_cord = (obj.location)
        request = self.context.get('request')
        currentUser = request.user
        user_cord = Profile.objects.filter(user=currentUser).values('location')[0]['location']
        R = 6373.0

        lat1 = radians(obj_cord[0])
        lon1 = radians(obj_cord[1])
        lat2 = radians(user_cord[0])
        lon2 = radians(user_cord[1])

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = R * c
        #print(currentUser)
        return (int(distance))

    class Meta:
        model = Profile
        read_only_fields = ('id',)
        fields = ["user","full_name", 'gender', 'distance' , 'location', 'email', 'profile_photo', 'match']


class MatchSerializer(serializers.ModelSerializer):
    #user1 = 
    class Meta:
        model= ProfileMatch
        fields = ('user1','user2','match_status')