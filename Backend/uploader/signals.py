from os import name
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import FileUpload
from pikepdf import Pdf, PdfError, PasswordError
import xml.etree.ElementTree as ET
import xml.dom.minidom


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


@receiver(post_save, sender=FileUpload)
def xmlfileupload(sender, instance, created, **kwargs):
    if created and instance.xml_file:
        files = instance.xml_file

        # doc = xml.dom.minidom.parse(files)
        # rows = doc.getElementsByTagName('employee')
        # print(rows.length)

        # for i in range(rows.length):
        #     name = doc.getElementsByTagName("firstname")[i]
        #     instance.read_name = instance.read_name+(name.firstChild.data)+" "
        #     title = doc.getElementsByTagName("title")[i]
        #     instance.read_email = instance.read_email + \
        #         (title.firstChild.data)+" "
        # room_no = doc.getElementsByTagName("room")[i]
        # instance.read_room_no = instance.read_room_no + \
        #     (room_no.firstChild.data)+" "
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
