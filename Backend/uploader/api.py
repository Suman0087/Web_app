from rest_framework import viewsets
from .models import FileUpload
from .serializers import FileUploadSerializer
# from rest_framework.pagination import PageNumberPagination


# class PostPagination(PageNumberPagination):
#     page_size = 10


class FileUploadViewset(viewsets.ModelViewSet):

    queryset = FileUpload.objects.all()
    serializer_class = FileUploadSerializer
    # pagination_class = PostPagination
