from celery import shared_task


@shared_task(bind=True)
def test_func(self):

    return "django_Celery_beat"
# from celery import shared_task
# from .models import FileUpload


# @shared_task(sender=FileUpload, bind=True)
# def pdf_file_uploads(created, instance):
#     # results = FileUpload.objects.all()
#     # if created:
#
#     # print('file is uploaded')

#     # file = instance.pdf_file

#     instance.is_pdf_file_uploaded = True

#     return "django_Celery_beat"
