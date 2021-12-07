from django.db import models


class FileUpload(models.Model):
    name = models.CharField(max_length=20)
    pdf_file = models.FileField(blank=True)
    is_password_protected = models.BooleanField(default=False)
    page_count = models.IntegerField(default=0)
    xml_file = models.FileField(blank=True)
    read_xml = models.TextField(blank=True)
    read_name = models.CharField(max_length=20, blank=True)
    read_email = models.EmailField(blank=True)
    read_gender = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return str(self.name)
