# from __future__ import absolute_import, unicode_literals
# import os
# from celery import Celery
# from django.conf import settings
# # from celery.schedules import crontab
# from kombu import Queue

# # Set the default Django settings module for the 'celery' program.
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_app.settings')

# app = Celery('web_app')

# app.config_from_object('django.conf:settings', namespace='CELERY')

# # Celery Beat Setting
# # app.conf.beat_schedule = {
# #     'send-task-every-minute': {
# #         'task': 'uploader.tasks.pdf_file_uploads',
# #         'schedule': crontab(),
# #     }

# # }

# app.conf.task_queues = (
#     Queue('upload', routing_key='upload'),

# )
# app.conf.task_routes = {
#     'task_queue.tasks.pdf_upload': {'queue': 'upload', 'routing_key': 'upload', },
# }

# # Load task modules from all registered Django apps.
# app.autodiscover_tasks()


# @app.task(bind=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')


import os

# import raven
from celery import Celery
from django.conf import settings
from dotenv import load_dotenv
# from raven.contrib.celery import register_logger_signal, register_signal
# from celery import signals

# Set the default Django settings module for the 'celery' program.
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_app.settings')


class CeleryCustomised(Celery):

    def on_configure(self):
        pass
        # client = raven.Client(str(os.getenv('SENTRY_DSN')))

        # # Always ensure you import register_logger_signal, register_signal and not their parent modules
        # # register a custom filter to filter out duplicate logs
        # register_logger_signal(client)

        # # hook into the Celery error handler
        # register_signal(client)


app = CeleryCustomised('epiback')


# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule = {}


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
