from rest_framework import permissions, generics, viewsets
from rest_framework.views import APIView

from app.models import Task, TaskApplication
from app.serializers import TaskSerializer, TaskApplicationSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """
    List all Tasks, or create a new one
    """
    permission_classes = [permissions.IsAuthenticated]

    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskApplicationViewSet(viewsets.ModelViewSet):
    """
    List all TaskApplications, or create a new one
    """
    permission_classes = [permissions.IsAuthenticated]

    queryset = TaskApplication.objects.all()
    serializer_class = TaskApplicationSerializer
