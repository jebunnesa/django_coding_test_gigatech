from django.urls import path, include
from .views import *
# from rest_framework import routers


# router = routers.DefaultRouter()
# router.register(r'work_day_plans', workDayApiView, 'work_day_plan')

urlpatterns = [
    path('workday_plan/delete/<int:pk>/', WorkPlanDeleteView.as_view(), name='workday_plan_delete'),
    path('signup', registerPage, name='signup'),
    path('logout/', log_out_page, name='logout'),
    path('login/', login_page, name='login'),
    path('work_plan/update/<int:pk>/', WorkPlanUpdateView.as_view(), name='work_plan_update'),
    # path('api', include(router.urls)),
    path('form_create', index, name='index'),
    path('', work_day_plan_List, name='work_day_plans')
]
