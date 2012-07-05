from django.contrib import admin
from django.db import models
class post(models.Model):
    title = models.CharField(max_length = 60)
    body = models.TextField()
    created = models.DateField(auto_now = True)
    updated = models.DateField(auto_now = True)

class comment(models.Model):
    body = models.TextField()
    author = models.CharField(max_length = 60)
    created = models.DateField(auto_now = True)
    updated = models.DateField(auto_now = True)
    post = models.ForeignKey(post)
