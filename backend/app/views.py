from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .models import Team
from .serializers import TeamSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the app index.")


class TeamPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = "page_size"


class TeamViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    pagination_class = TeamPagination
