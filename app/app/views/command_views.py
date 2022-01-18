from rest_framework import permissions, viewsets

from app.models import Command
from app.serializers import CommandSerializer


class CommandViewSet(viewsets.ModelViewSet):
    """
    List all Commands, or create a new one
    """
    permission_classes = [permissions.IsAuthenticated]

    queryset = Command.objects.all()
    serializer_class = CommandSerializer
