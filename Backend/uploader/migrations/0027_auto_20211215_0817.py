# Generated by Django 3.2.8 on 2021-12-15 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0026_alter_fileupload_read_xml'),
    ]

    operations = [
        migrations.CreateModel(
            name='XMLFileUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xml_name', models.CharField(default=None, max_length=20)),
                ('xml_file', models.FileField(blank=True, upload_to='')),
                ('read_xml', models.TextField(blank=True)),
                ('read_name', models.CharField(blank=True, max_length=20)),
                ('read_title', models.CharField(blank=True, max_length=20)),
                ('read_div', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='fileupload',
            name='read_div',
        ),
        migrations.RemoveField(
            model_name='fileupload',
            name='read_name',
        ),
        migrations.RemoveField(
            model_name='fileupload',
            name='read_title',
        ),
        migrations.RemoveField(
            model_name='fileupload',
            name='read_xml',
        ),
        migrations.RemoveField(
            model_name='fileupload',
            name='xml_file',
        ),
    ]
