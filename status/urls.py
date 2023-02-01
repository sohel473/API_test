from django.urls import path
from .views import StatusAPIView

urlpatterns = [
    path("api/", StatusAPIView.as_view()),
]