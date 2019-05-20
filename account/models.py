from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from datetime import datetime


class Profile(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,verbose_name='User',related_name='profile')
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    image = models.ImageField(upload_to='users/image/%Y/%m/%d', verbose_name='Profile image',blank=True,null=True, default='users/image/no-pic.png')
    birthday = models.DateField(verbose_name='Date of Birth', blank=True, null=True)

    def __str__(self):
        return 'Profile {}'.format(self.user.username)
