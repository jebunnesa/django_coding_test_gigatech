from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class TimeInput(forms.TimeInput):
    input_type = 'time'


class DateInput(forms.DateInput):
    input_type = 'date'


class workDayPlanForm(forms.ModelForm):
    class Meta:
        model = WorkDayPlan
        fields = ['start_time', 'end_time', 'to_do', 'work']
        widgets = {
            'start_time': TimeInput(),
            'end_time': TimeInput(),
        }