from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from app import views

urlpatterns = [
    path('applications/', views.ApplicationList.as_view()),
    path('applications/<int:pk>/', views.ApplicationDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)