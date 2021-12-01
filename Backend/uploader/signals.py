from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import FileUpload
from pikepdf import Pdf, PdfError, PasswordError


@receiver(post_save, sender=FileUpload)
def fileupload(sender, instance, created, **kwargs):
    if created and instance.document:
        print('file is uploaded')
        file = instance.document

        try:
            count = Pdf.open(file)
            instance.page_count = len(count.pages)
        except PasswordError:
            instance.is_password_protected = True
        except Exception as e:
            print(e)
        instance.save()
