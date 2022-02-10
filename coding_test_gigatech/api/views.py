from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .serializers import WorkDaySerializer
from to_do.models import WorkDayPlan
# from .pagination import PostLimitOffsetPagination


class WorkDayViewSet(viewsets.ModelViewSet):
    queryset = WorkDayPlan.objects.all()
    serializer_class = WorkDaySerializer
    # pagination_class = PostLimitOffsetPagination
    http_method_names = ['get', 'head', 'post', 'patch', 'update', 'delete']

