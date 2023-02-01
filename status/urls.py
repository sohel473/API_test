from django.urls import path
from .views import StatusAPIView, StatusCreateAPIView, StatusListAPIView

urlpatterns = [
    path("status/", StatusAPIView.as_view()),
    path("status/list/", StatusListAPIView.as_view()),
    path("status/create/", StatusCreateAPIView.as_view()),
]