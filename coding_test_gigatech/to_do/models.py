from django.db import models
# from django.utils import timezone
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='%(app_label)s_%(class)s_modified_by', null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='%(app_label)s_%(class)s_created_by', null=True, blank=True)
    active_status = models.BooleanField(default=True)

    class Meta:
        abstract = True


class WorkDayPlan(BaseModel):
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    Date = models.DateField(auto_now=True)
    to_do = models.CharField(max_length=100)
    work = models.CharField(max_length=100, verbose_name='Purpose')

    def __str__(self):
        return self.to_do

