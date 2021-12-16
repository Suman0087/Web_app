from django.contrib import admin
from .models import FileUpload, XMLFileUpload

admin.site.register(FileUpload)
admin.site.register(XMLFileUpload)
