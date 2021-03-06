from .models import FileUpload, XMLFileUpload
from web_app.celery import app
from celery import shared_task
from pikepdf import Pdf

# @app.task(queue='uplaod')


@shared_task(bind=True)
def pdf_file_uploads(self, id):
    # pdf_file_upload.delay()
    obj = FileUpload.objects.get(id=id)
    obj.is_pdf_file_uploaded = True
    try:
        file = obj.pdf_file
        count = Pdf.open(file)
        obj.page_count = len(count.pages)
        obj.is_pdf_file_uploaded = True
        obj.pdf_total_page_count_checked = True

    except Exception as e:
        print(e)
    # obj.pdf_total_page_count_checked = True
    obj.pdf_file_saved = True
    obj.save()
    return "pdf uploaded"


@shared_task(bind=True)
def xml_file_uploaded(self, id):
    # pdf_file_upload.delay()
    obj = XMLFileUpload.objects.get(id=id)
    obj.is_xml_file_uploaded = True
    obj.xml_parse_completed = True
    obj.xml_name_parse_completed = True
    obj.xml_title_parse_completed = True
    obj.save()
    return "xml uploaded"
