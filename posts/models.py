# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ckeditor_uploader.fields import RichTextUploadingField

from django.db import models

from datetime import  datetime

# Create your models here.


class Posts(models.Model):
    title = models.CharField(max_length=200)
    body = RichTextUploadingField()
    image = models.ImageField(default='default.png',blank=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Posts'