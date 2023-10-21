from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class ProfilePageModel(models.Model):
	user = models.OneToOneField(User, primary_key=True, verbose_name='user', related_name='userprofile', on_delete=models.CASCADE)
	name = models.CharField(max_length=32, blank=True, null=True)
	title = models.CharField(max_length=64, blank=True, null=True)
	bio = models.TextField(max_length=512, blank=True, null=True)
	birth_date = models.DateField(blank=True, null=True)
	joining_date = models.DateField(default=date.today, blank=True, null=True)
	profile_picture = models.ImageField(upload_to='uploads/userprofile/profile_pictures', default='uploads/userprofile/profile_pictures/default.png', blank='True')
	cover_picture = models.ImageField(upload_to='uploads/userprofile/cover_pictures', default='uploads/userprofile/cover_pictures/default.png', blank='True')

@receiver(post_save, sender=User)
def create_user_profile_page(sender, instance, created, **kwargs):
	if created:
		ProfilePageModel.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile_page(sender, instance, **kwargs):
	instance.userprofile.save
	