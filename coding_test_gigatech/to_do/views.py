from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
# from rest_framework import viewsets
# from .serializers import *
from .models import *
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import UserCreationForm
# from .forms import CreateUserForm
from django.urls import reverse_lazy

from datetime import date
# Create your views here.

import json
import urllib.request


def get_weather_data():
    source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=Dhaka&appid=48c5c197cdf693845ce51ff8794494a1').read()
    # converting JSON data to a dictionary
    list_of_data = json.loads(source)
    temp = round(list_of_data['main']['temp'] - 273.15, 2)
    #data for variable list_of_data
    data = {
        "temp": str(temp),
        "status": list_of_data['weather'][0]['main'],
        "humidity": str(list_of_data['main']['humidity']),
    }
    return data

@method_decorator(login_required(login_url='login'), name='dispatch')
class WorkPlanDeleteView(DeleteView):
    model = WorkDayPlan
    template_name = "workday_plan_delete_form.html"
    success_url = reverse_lazy('work_day_plans')


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('work_day_plans')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'signup.html', context)


def log_out_page(request):
    logout(request)
    return redirect('login')


def login_page(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        userName = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=userName, password=password)
        if user is not None:
            login(request, user)
            return redirect("work_day_plans")

        else:
            messages.info(request, 'Invalid username or password!')

    return render(request, 'login_with_password.html', {})


@method_decorator(login_required(login_url='login'), name='dispatch')
class WorkPlanUpdateView(UpdateView):
    model = WorkDayPlan
    form_class = workDayPlanForm
    # fields = ['start_time', 'end_time', 'to_do', 'work']
    template_name = "work_plan_update_form.html"
    success_url = '/'


@login_required(login_url='login')
def work_day_plan_List(request):
    weather_data = get_weather_data()
    plan_list = WorkDayPlan.objects.all().filter(created_by=request.user).order_by('start_time')
    return render(request, 'workDayPlanList.html', {'work_day_plans': plan_list, 'weather_data': weather_data})


# @method_decorator(login_required(login_url='login'), name='dispatch')
# class workDayApiView(viewsets.ModelViewSet):
#     serializer_class = workDayPlanSerializer
#     queryset = WorkDayPlan.objects.all()


@login_required(login_url='login')
def index(request):
    if request.method == 'POST':
        form = workDayPlanForm(request.POST)
        if form.is_valid():
            row = form.save(commit=False)
            row.created_by = request.user
            row.save()
            return redirect('work_day_plans')
    else:
        form = workDayPlanForm()
    return render(request, 'workDayPlanForm.html', {'form': form, })

