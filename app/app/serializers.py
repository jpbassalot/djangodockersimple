from rest_framework import serializers
from .models import *


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['id', 'name', 'description', 'created_at', 'updated_at']
