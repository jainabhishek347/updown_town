from rest_framework import serializers
from django.contrib.auth.models import User
from profiles.models import Profile, ProfileMatch


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email',  'first_name', 'last_name']

class ProfileSerializerCommon(serializers.ModelSerializer):
    profile_photo = serializers.ImageField()
    user_id = UserSerializer(many=False, read_only=True)
    class Meta:
        model = Profile
        geo_field = "location"
        fields = ["full_name", 'gender', 'location', 'profile_photo','user_id']


class ProfileMatchSerializer(serializers.ModelSerializer):
    match_profile = ProfileSerializerCommon(many=False, read_only=True)
    class Meta:
        model = ProfileMatch
        fields = ('match_profile', 'match_status', 'created_at', 'updated_at')

class ProfileSerializer(serializers.ModelSerializer):
    profile_photo = serializers.ImageField()
    requested_profile = ProfileMatchSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        geo_field = "location"
        read_only_fields = ('id',)
        fields = ["full_name", 'gender' , 'location', 'email', 'profile_photo', 'requested_profile']
