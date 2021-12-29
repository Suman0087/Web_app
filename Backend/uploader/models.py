from django.db import models
from django.db.models.base import Model
from django.db.models.expressions import F


class FileUpload(models.Model):
    name = models.CharField(max_length=20)
    pdf_file = models.FileField(blank=True)
    is_pdf_file_uploaded = models.BooleanField(default=False)
    is_password_protected = models.BooleanField(default=False)
    page_count = models.IntegerField(default=0)

    def __str__(self):
        return str(self.name)


class XMLFileUpload(models.Model):
    xml_name = models.CharField(default=None, max_length=20)
    xml_file = models.FileField(blank=True)
    read_xml = models.TextField(blank=True)
    read_name = models.TextField(blank=True)
    read_title = models.TextField(blank=True)
    read_div = models.TextField(blank=True)

    def __str__(self):
        return str(self.xml_name)
