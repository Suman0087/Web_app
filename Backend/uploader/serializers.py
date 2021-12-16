from rest_framework import serializers
from .models import FileUpload, XMLFileUpload


class FileUploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = FileUpload
        fields = '__all__'


class XMLFileUploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = XMLFileUpload
        fields = '__all__'
