from rest_framework import permissions
from rest_framework import viewsets

from rest_framework import filters
from django.contrib.gis.measure import Distance

from django.contrib.gis.geos import Point
from django_filters.rest_framework import DjangoFilterBackend
from profiles.serializers import *
from profiles.models import *


    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = []
    permission_classes = [permissions.IsAuthenticated]

class ListProfileViewSet(viewsets.ModelViewSet):
    #queryset = Profile.objects.all()
    serializer_class = ListSerializer
    http_method_names = ['get']
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    permission_classes = [permissions.IsAuthenticated]
    ordering_fields =["full_name", 'gender' , 'email', 'match']
    filterset_fields =["full_name", 'gender', 'email', 'match']
    def get_queryset(self):
        currentUser = self.request.user
        return Profile.objects.exclude(user = currentUser)

class CreateProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    http_method_names = ['post']
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    permission_classes = [permissions.IsAuthenticated]
    ordering_fields =['user',"full_name", 'gender' , 'location', 'email', 'profile_photo', 'match']
    filterset_fields =['user',"full_name", 'gender' , 'location', 'email', 'profile_photo', 'match']

class MatchProfileViewSet(viewsets.ModelViewSet):
    queryset = ProfileMatch.objects.all()
    serializer_class = MatchSerializer
    #http_method_names = ['post']
    #first snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)
    #user1 = ProfileSerializer(many=True,read_only=True)
    #user2 = ProfileSerializer(many=True,read_only=True)
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    permission_classes = [permissions.IsAuthenticated]
    ordering_fields =['user1','user2', 'match_status']
    filterset_fields =['user1','user2', 'match_status']

