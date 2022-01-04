# Generated by Django 3.2.8 on 2022-01-03 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0029_fileupload_is_pdf_file_uploaded'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileupload',
            name='pdf_file_saved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='fileupload',
            name='pdf_total_page_count_checked',
            field=models.BooleanField(default=False),
        ),
    ]
