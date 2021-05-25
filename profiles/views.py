from rest_framework.generics import GenericAPIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework import permissions

from django.contrib.gis.measure import Distance

from django.contrib.gis.geos import Point
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from profiles.serializers import ProfileSerializer
from profiles.models import Profile, ProfileMatch

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100

# Create your views here.

class CommonProfileAPIView(GenericAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    ordering_fields = ['gender',]
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['gender']
    pagination_class = StandardResultsSetPagination

class ListProfileAPIView(CommonProfileAPIView, ListAPIView):
    """This endpoint list all of the available todos from the database"""

    def get_queryset(self) :
        """
        Filter profiles based on longitude, latitude and radius. If any of them not provided thjen return all results.
        :return: query_set
        """
        longitude = self.request.query_params.get('longitude')
        latitude= self.request.query_params.get('latitude')
        radius = self.request.query_params.get('radius')
        if longitude and latitude and  radius:
            loca = Point(float(longitude), float(latitude))
            queryset = Profile.objects.filter(location__distance_lt=(loca, Distance(km=radius)))
        else:
            queryset = Profile.objects.all()
        return queryset

class CreateProfileAPIView(CreateAPIView):
    """This endpoint allows for creation of a todo"""
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class UpdateTodoAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific todo by passing in the id of the todo to update"""
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class MatchProfileAPIView(CommonProfileAPIView):
    """This endpoint allows for deletion of a specific Todo from the database"""
    queryset = ProfileMatch.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self) :
        """
        Filter profiles based on longitude, latitude and radius. If any of them not provided thjen return all results.
        :return:
        """
        profile_id = self.request.query_params.get('profile_id')
        match = self.request.query_params.get('match')
        if profile_id and match:
            queryset = Profile.objects.filter(location__distance_lt=(loca, Distance(km=radius)))
        else:
            queryset = Profile.objects.all()
        return queryset