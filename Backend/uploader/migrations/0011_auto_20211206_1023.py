# Generated by Django 3.2.8 on 2021-12-06 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0010_auto_20211130_0946'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileupload',
            name='read_xml',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='fileupload',
            name='xml_file',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
