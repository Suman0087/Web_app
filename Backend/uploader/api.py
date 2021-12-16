from rest_framework import viewsets
from .models import FileUpload, XMLFileUpload
from .serializers import FileUploadSerializer, XMLFileUploadSerializer
from rest_framework.pagination import PageNumberPagination


class PostPagination(PageNumberPagination):
    page_size = 10


class FileUploadViewset(viewsets.ModelViewSet):

    queryset = FileUpload.objects.all()
    serializer_class = FileUploadSerializer
    pagination_class = PostPagination


class XMLFileUploadViewset(viewsets.ModelViewSet):

    queryset = XMLFileUpload.objects.all()
    serializer_class = XMLFileUploadSerializer
    pagination_class = PostPagination
