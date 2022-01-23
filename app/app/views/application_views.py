from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework import permissions

from app.models import Application
from app.serializers import ApplicationSerializer


def api_root(request):
    return HttpResponse('404 Not Found')


class ApplicationViewSet(viewsets.ModelViewSet):
    """
    List all Applications, or create a new one
    """
    permission_classes = [permissions.IsAuthenticated]

    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
