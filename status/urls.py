from django.urls import path
# from .views import (
#     StatusAPIView,
#     StatusListAPIView,
#     StatusCreateAPIView,
#     StatusDetailAPIView,
#     StatusUpdateAPIView,
#     StatusDeleteAPIView,
# )

from .views import (
    StatusDetailAPIView,
    StatusListCreateView,
)

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

urlpatterns = [
    path("status/", StatusListCreateView.as_view()),
    path("status/<id>/", StatusDetailAPIView.as_view()),
]