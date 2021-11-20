from rest_framework import viewsets
from .models import FileUpload
from .serializers import FileUploadSerializer

class FileUploadViewset(viewsets.ModelViewSet):
 
    queryset = FileUpload.objects.all()
    serializer_class = FileUploadSerializer