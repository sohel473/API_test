from .models import Status  # Model
from .serializers import StatusSerializer  # Serializer based on Status Model

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import generics, mixins

# Create your views here.


class StatusListCreateView(mixins.CreateModelMixin, generics.ListAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StatusDetailAPIView(
    mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.RetrieveAPIView
):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    lookup_field = "id"

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# class StatusAPIView(APIView):
#     def get(self, request, format=None):
#         status_list = Status.objects.all()
#         status_serializer = StatusSerializer(status_list, many=True)
#         return Response(status_serializer.data)


# class StatusListAPIView(generics.ListAPIView):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer


# class StatusCreateAPIView(generics.CreateAPIView):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer

# class StatusDetailAPIView(generics.RetrieveAPIView):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     lookup_field = "id"

#     # def get_object(self, *args, **kwargs):
#     #     kwargs = self.kwargs
#     #     kw_id = kwargs.get("id")
#     #     return Status.objects.get(id=kw_id)


# class StatusUpdateAPIView(generics.UpdateAPIView):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     lookup_field = "id"


# class StatusDeleteAPIView(generics.DestroyAPIView):
#     queryset = Status.objects.all()
#     serializer_class = StatusSerializer
#     lookup_field = "id"