# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ckeditor_uploader.fields import RichTextUploadingField

from django.db import models

from datetime import  datetime
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = RichTextUploadingField()
    image = models.ImageField(default='default.png',blank=True)
    created_at = models.DateTimeField(default=datetime.now,blank=True)
    author = models.ForeignKey(User,default=None,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Posts'