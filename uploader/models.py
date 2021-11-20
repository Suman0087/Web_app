from django.db import models

class FileUpload(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    document = models.FileField(blank=True)
