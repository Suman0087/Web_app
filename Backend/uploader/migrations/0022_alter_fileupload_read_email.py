# Generated by Django 3.2.8 on 2021-12-14 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0021_auto_20211214_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='read_email',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
