from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

from .views import *
from rest_framework.authtoken import views

router = routers.DefaultRouter()

router.register(r'work_day_plans', WorkDayViewSet, 'visitors')

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
    path('', include(router.urls)),
]