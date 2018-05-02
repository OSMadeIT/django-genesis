# Generated by Django 2.0.3 on 2018-03-30 19:55

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20180328_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='thumb',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='posts',
            name='body',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]