from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class ApplicationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Application
        fields = ['id', 'name', 'description', 'created_at', 'updated_at']


class CommandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Command
        fields = ['id', 'command']


class TaskApplicationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = TaskApplication
        fields = ['id', 'application', 'command', 'name', 'created_at', 'updated_at']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'task_application', 'status', 'created_at', 'updated_at']
