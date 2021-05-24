from django.urls import include
from django.urls import path
from profiles import views

from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'', views.ProfileViewSet)

urlpatterns = [
    path("", include(router.urls)),
]