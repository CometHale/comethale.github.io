from __future__ import unicode_literals
from django.db import models

class Post(models.Model):
	text = models.TextField()
	publish_datetime = models.DateTimeField(auto_now_add=True)
	edit_datetime = models.DateTimeField(auto_now=True)

