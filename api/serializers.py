from rest_framework import serializers
from .models import Task, FinishedTask

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class FinishedTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinishedTask
        fields = '__all__'