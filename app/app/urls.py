from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app.views.application_views import ApplicationViewSet
from app.views.command_views import CommandViewSet
from app.views.task_views import TaskApplicationViewSet, TaskViewSet
from app.views.user_views import UserViewSet

router = DefaultRouter()
router.register(r'applications', ApplicationViewSet)
router.register(r'users', UserViewSet)
router.register(r'task-applications', TaskApplicationViewSet)
router.register(r'commands', CommandViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
