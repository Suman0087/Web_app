# Generated by Django 3.2.8 on 2021-12-28 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0028_auto_20211227_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileupload',
            name='is_pdf_file_uploaded',
            field=models.BooleanField(default=False),
        ),
    ]
