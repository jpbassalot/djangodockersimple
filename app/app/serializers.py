from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from .models import *


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'task_application', 'status', 'created_at', 'updated_at']


class CommandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Command
        fields = ['id', 'command']


class ApplicationSerializer(serializers.ModelSerializer):
    task_application_set = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='taskapplication-detail')

    class Meta:
        model = Application
        fields = ['id', 'name', 'description', 'task_application_set', 'created_at', 'updated_at']


class TaskApplicationSerializer(serializers.ModelSerializer):
    application = ApplicationSerializer(read_only=True)

    class Meta:
        model = TaskApplication
        fields = ['id', 'application', 'command', 'name', 'created_at', 'updated_at']
