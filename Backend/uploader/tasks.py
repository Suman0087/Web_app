from .models import FileUpload, XMLFileUpload
from web_app.celery import app
from celery import shared_task


# @app.task(queue='uplaod')
@shared_task(bind=True)
def pdf_file_uploads(self, id):
    # pdf_file_upload.delay()
    obj = FileUpload.objects.get(id=id)
    obj.is_pdf_file_uploaded = True
    obj.pdf_file_saved = True
    obj.save()
    return "pdf uploaded"


@shared_task(bind=True)
def xml_file_uploaded(self, id):
    # pdf_file_upload.delay()
    obj = XMLFileUpload.objects.get(id=id)
    obj.is_xml_file_uploaded = True
    obj.xml_parse_completed = True
    obj.save()
    return "xml uploaded"
