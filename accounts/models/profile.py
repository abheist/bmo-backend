import uuid

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField

from accounts import GENDER_CHOICES
from accounts.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    address1 = models.CharField(max_length=1024)
    address2 = models.CharField(max_length=1024)
    zip_code = models.CharField(max_length=12)
    city = models.CharField(max_length=1024)
    country = CountryField()

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
