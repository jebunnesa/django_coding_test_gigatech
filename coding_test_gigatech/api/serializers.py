from to_do.models import WorkDayPlan
from rest_framework import serializers


class WorkDaySerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkDayPlan
        fields = '__all__'

