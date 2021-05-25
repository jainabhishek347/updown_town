from django.urls import include
from django.conf.urls import url
from django.urls import path
from profiles import views

from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'create', views.CreateProfileViewSet, basename='create')
router.register(r'list', views.ListProfileViewSet, basename='list')
router.register(r'match', views.MatchProfileViewSet, basename='match')
#router.register(r'users', views.UserViewSet, basename='user')

urlpatterns = [
    url('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

# path("",views.ListTodoAPIView.as_view(),name="todo_list"),
# path("create/", views.CreateTodoAPIView.as_view(),name="todo_create"),
# path("update/<int:pk>/",views.UpdateTodoAPIView.as_view(),name="update_todo"),
# path("delete/<int:pk>/",views.DeleteTodoAPIView.as_view(),name="delete_todo")
