from rest_framework import serializers
from profiles.models import Profile



class ProfileSerializer(serializers.ModelSerializer):
    profile_photo = serializers.ImageField()

    class Meta:
        model = Profile
        geo_field = "location"
        fields = ["full_name", 'gender' , 'location', 'email', 'profile_photo']
