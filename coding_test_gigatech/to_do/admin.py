from django.contrib import admin
from .models import WorkDayPlan
# Register your models here.


class WorkDayAdmin(admin.ModelAdmin):
    fields = ['start_time', 'end_time',  'to_do', 'work', ]

    list_display = ['start_time', 'end_time', 'Date', 'to_do', 'work', 'created_by',]


admin.site.register(WorkDayPlan, WorkDayAdmin)