from django.urls import path
# from .views import (
#     StatusAPIView,
#     StatusListAPIView,
#     StatusCreateAPIView,
#     StatusDetailAPIView,
#     StatusUpdateAPIView,
#     StatusDeleteAPIView,
# )

# urlpatterns = [
#     path("status/", StatusAPIView.as_view()),
#     path("status/list/", StatusListAPIView.as_view()),
#     path("status/create/", StatusCreateAPIView.as_view()),
#     path("status/detail/<id>/", StatusDetailAPIView.as_view()),
#     path("status/update/<id>/", StatusUpdateAPIView.as_view()),
#     path("status/delete/<id>/", StatusDeleteAPIView.as_view()),
# ]

# status/ -> List, Create => GET, POST
# status/<id>/ -> Details, Delete, Update => GET, DELETE, PUT/PATCH

# from .views import (
#     StatusDetailUpdateDeleteView,
#     StatusListCreateView,
# )

# urlpatterns = [
#     path("status/", StatusListCreateView.as_view()),
#     path("status/<id>/", StatusDetailUpdateDeleteView.as_view()),
# ]

from .views import StatusViewset
from rest_framework.routers import DefaultRouter

# status/ -> List, Create => GET, POST
# status/<id>/ -> Details, Delete, Update => GET, DELETE, PUT/PATCH

router = DefaultRouter()
router.register(r"status", StatusViewset, basename="status")

urlpatterns = [] + router.urls