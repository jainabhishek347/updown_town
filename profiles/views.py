from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework import permissions
from rest_framework import viewsets

#from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.measure import Distance

from django.contrib.gis.geos import Point
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination


from profiles.serializers import ProfileSerializer
from profiles.models import Profile


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 25
    page_size_query_param = 'page_size'
    max_page_size = 100

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    ordering_fields = ['gender',]
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['gender']# 'location', ]
    pagination_class = StandardResultsSetPagination


    def get_queryset(self):
        longitude = self.request.query_params.get('longitude',1.0)
        latitude= self.request.query_params.get('latitude', 52.5)
        radius = self.request.query_params.get('radius', 10)

        #location = Point(longitude, latitude)
        loca = Point(1.0, 52.5)
        radius =10

        #queryset = Resturent.objects.annotate(distance=Distance('location',user_location)).order_by('distance')[0:100]
        #queryset = Profile.objects.filter(location__distance_lte=(location, Distance(m=radius))).distance(location).order_by('distance')
        queryset = Profile.objects.filter(location__distance_lt=(loca, Distance(km=radius)))

        return queryset

# Create your views here.
class ListTodoAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


class CreateTodoAPIView(CreateAPIView):
    """This endpoint allows for creation of a todo"""
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class UpdateTodoAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific todo by passing in the id of the todo to update"""
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class DeleteTodoAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Todo from the database"""
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]