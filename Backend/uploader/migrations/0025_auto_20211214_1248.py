# Generated by Django 3.2.8 on 2021-12-14 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0024_alter_fileupload_xml_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='read_xml',
            field=models.TextField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='fileupload',
            name='xml_file',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
