from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions

from app.serializers import UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    permission_classes = [permissions.IsAuthenticated]
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
