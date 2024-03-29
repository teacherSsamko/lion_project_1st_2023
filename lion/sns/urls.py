from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r"posts", views.PostViewSet)

urlpatterns = [
    path("follow/", views.FollowView.as_view(), name="follow"),
    path("feed/", views.FeedView.as_view(), name="feed"),
] + router.urls
