"""coding_test_gigatech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path


admin.site.site_header = "TO DO"
admin.site.site_title = "To_DO Admin Portal"
admin.site.index_title = "Welcome to TO_DO app"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  include('to_do.urls')),
]

# from django.contrib import admin
# from django.urls import include, path
# from django.contrib.auth import views as auth_views #import this
#
# admin.site.site_header = "Day Plan"
# admin.site.site_title = "Day Plan Admin Portal"
# admin.site.index_title = "Welcome to Day Plan"
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',  include('plan.urls')),
#     # path('password_reset/', auth_views.password_reset, name='password_reset'),
#     path('password_reset/done/',
#          auth_views.PasswordResetDoneView.as_view(),
#          name='password_reset_done'),
#     path('reset/<uidb64>/<token>/',
#          auth_views.PasswordResetConfirmView.as_view(template_name="main/password/password_reset_confirm.html"),
#          name='password_reset_confirm'),
#     path('reset/done/',
#          auth_views.PasswordResetCompleteView.as_view(template_name='main/password/password_reset_complete.html'),
#          name='password_reset_complete'),
#
# ]
