from django.db import models

# Create your models here.

#Model to integrate UStream Videos
class UstreamListing(models.Model):
    ustream_uid = models.IntegerField(default=0)
    title = models.CharField(max_length=200)
    is_protected = models.NullBooleanField(default=False)
    url = models.CharField(max_length=200)
    description = models.CharField(max_length=600)
    status = models.CharField(max_length=10)
    image_url = models.CharField(max_length=200)
    emergency_contact = models.IntegerField(default=0)
    location_description = models.CharField(max_length=200)


class UserProfile(models.Model):
    karma = models.IntegerField(default=0, verbose_name="Karma Points")