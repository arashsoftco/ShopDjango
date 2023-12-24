from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    avatar = models.ImageField(upload_to='images/profile', verbose_name='Image Avatar', null=True, blank=True)
    email_active_code = models.CharField(max_length=100, verbose_name="active code from email")
    about_user = models.TextField(null=True, blank=True, verbose_name='inWither person')
    address = models.TextField(null=True, blank=True, verbose_name='Address')

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        if self.first_name is not '' and self.last_name is not '':
            return self.get_full_name()

        return self.email
