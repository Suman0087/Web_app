from django.db import models


class FileUpload(models.Model):
    name = models.CharField(max_length=20)
    document = models.FileField(blank=True)
    is_password_protected = models.BooleanField(default=False)
    page_count = models.IntegerField(default=0)

    def __str__(self):
        return str(self.name)
