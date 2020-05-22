from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.TextField(max_length=500, blank=True)
	address = models.CharField(max_length=30, blank=True)
	birth_date = models.DateField(null=True, blank=True)
	email = models.EmailField(unique=True, blank=False)
	email_confirmed = models.BooleanField(default=False)

	def __str__(self):
		return str(self.user)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)
	instance.profile.save()

	