from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import permissions

from app.models import Application
from app.serializers import ApplicationSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'applications': reverse('application-list', request=request, format=format)
    })


class ApplicationViewSet(viewsets.ModelViewSet):
    """
    List all Applications, or create a new one
    """
    permission_classes = [permissions.IsAuthenticated]

    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
