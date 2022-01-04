from os import name
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import FileUpload, XMLFileUpload
from pikepdf import Pdf, PdfError, PasswordError
import xml.etree.ElementTree as ET
from .tasks import pdf_file_uploads
from .tasks import xml_file_uploaded


@receiver(post_save, sender=FileUpload)
def fileupload(sender, instance, created, **kwargs):
    if created and instance.pdf_file:

        print('file is uploaded')
        file = instance.pdf_file

        try:
            count = Pdf.open(file)
            instance.page_count = len(count.pages)
            instance.pdf_total_page_count_checked = True
        except PasswordError:
            instance.is_password_protected = True

        except Exception as e:
            print(e)
        instance.save()


@receiver(post_save, sender=FileUpload)
def pdf_file_upload(sender, instance, created, **kwargs):
    if created:
        # instance.is_pdf_file_uploaded = True
        pdf_file_uploads.delay(instance.id)
        # try:

        #     pdf_file_uploads.delay(instance.id)
        # except PasswordError:
        #     pdf_file_uploads(instance.id)


@receiver(post_save, sender=XMLFileUpload)
def xmlfileupload(sender, instance, created, **kwargs):
    if created and instance.xml_file:
        files = instance.xml_file
        read = ET.parse(files)
        texts = read.getroot()
        elements = []

        for element in texts:
            for subelement in element:
                elements.append(subelement.text)
                instance.read_xml = elements
            element.findtext('firstname')
            instance.read_name = instance.read_name + \
                (element.findtext('firstname'))+" "
            element.findtext('title')
            instance.read_title = instance.read_title + \
                (element.findtext('title'))+" "
            element.findtext('division')
            instance.read_div = instance.read_div + \
                (element.findtext('division'))+" "

        instance.save()


@receiver(post_save, sender=XMLFileUpload)
def xml_files(sender, instance, created, **kwargs):
    if created:
        # instance.is_pdf_file_uploaded = True
        try:
            xml_file_uploaded.delay(instance.id)
        except AttributeError:
            xml_file_uploaded(instance.id)
