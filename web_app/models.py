from django.db import models

# Create your models here.

#Model to integrate UStream Videos
class UStream(models.Model):
	ustream_id = models.IntegerField(default=0)
	title = models.CharField(max_length=200)
	is_protected = models.NullBooleanField(default=False)
	url = models.CharField(max_length=200)
	description = models.CharField(max_length=600)
	status = models.CharField(max_length = 10)
	image_url_small = models.CharField(max_length=200)
	image_url_big = models.CharField(max_length=200)