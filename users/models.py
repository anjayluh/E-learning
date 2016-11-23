from django.db import models
# Create your models here.
from django.contrib.auth.models import User
class UserProfile(models.Model):
    # Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    country = models.URLField(blank=True, name = 'Country')
    picture = models.ImageField(upload_to='profile_images', blank=True, name = 'Profile')

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username