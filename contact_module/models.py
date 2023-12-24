from django.db import models


# Create your models here.

class ContactUs(models.Model):
    title = models.CharField(max_length=300, verbose_name='Title')
    email = models.EmailField(max_length=300, verbose_name='email')
    full_name = models.CharField(max_length=300, verbose_name='name and name family')
    message = models.TextField(verbose_name='Text contact us')
    created_date = models.DateTimeField(verbose_name='Date Creation', auto_now_add=True)
    response = models.TextField(verbose_name='Text Response contact us', null=True, blank=True)
    is_read_by_admin = models.BooleanField(verbose_name='Read by admin', default=False)

    class Meta:
        verbose_name = 'contact us'
        verbose_name_plural = 'list contact us'

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    image = models.ImageField(upload_to='images')
