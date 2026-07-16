from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register("teams", views.TeamViewSet, basename="team")

urlpatterns = [
    path("", views.index, name="index"),
    path("api/", include(router.urls)),
]
