from django.urls import include
from django.urls import path
from profiles import views

from rest_framework import routers
router = routers.DefaultRouter()
#router.register(r'', views.ProfileViewSet)

urlpatterns = [
    path("list/", views.ListProfileAPIView.as_view(),name="profile_list"),
    path("create/", views.CreateProfileAPIView.as_view(),name="profile_create"),
    path("match/", views.MatchProfileAPIView.as_view(),name="profile_match"),
    #path("", include(router.urls)),
]

# path("",views.ListTodoAPIView.as_view(),name="todo_list"),
# path("create/", views.CreateTodoAPIView.as_view(),name="todo_create"),
# path("update/<int:pk>/",views.UpdateTodoAPIView.as_view(),name="update_todo"),
# path("delete/<int:pk>/",views.DeleteTodoAPIView.as_view(),name="delete_todo")
