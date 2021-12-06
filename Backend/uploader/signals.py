from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import FileUpload
from pikepdf import Pdf, PdfError, PasswordError
import xml.etree.ElementTree as ET


@receiver(post_save, sender=FileUpload)
def fileupload(sender, instance, created, **kwargs):
    if created and instance.pdf_file:
        print('file is uploaded')
        file = instance.pdf_file

        try:
            count = Pdf.open(file)
            instance.page_count = len(count.pages)
        except PasswordError:
            instance.is_password_protected = True
        except Exception as e:
            print(e)
        instance.save()


# @receiver(post_save, sender=FileUpload)
# def fileupload(sender, instance, created, **kwargs):
    if created and instance.xml_file:
        files = instance.xml_file
        read = ET.parse(files)
        text = read.getroot()
        elements = []
        print(text)
        for element in text:
            for subelement in element:
                elements.append(subelement.text)
        instance.read_xml = elements
        instance.save()
