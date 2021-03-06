from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	avatar = models.ImageField(upload_to="avatars", null=True, blank=True)
	bio = models.TextField(max_length=500, default='', blank=True)
	location = models.CharField(max_length=100, default='', blank=True)
	remaining_quota = models.IntegerField(default=3, blank=True) #  quota - total number of images uploaded by this account
	daily_upload_count = models.IntegerField(default=0, blank=True) # the number of images uploaded on that day, 4
	last_upload_time = models.DateTimeField(default = datetime.now(), null=True, blank=True)
	curator = models.BooleanField(default=0, blank=True)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
	instance.profile.save()
