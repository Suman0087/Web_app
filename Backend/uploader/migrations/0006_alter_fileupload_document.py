# Generated by Django 3.2.8 on 2021-11-29 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0005_alter_fileupload_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='document',
            field=models.FileField(blank=True, default=False, upload_to=''),
            preserve_default=False,
        ),
    ]