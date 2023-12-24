from django.db import models


# Create your models here.

class SiteSetting(models.Model):
    site_name = models.CharField(max_length=200, verbose_name='name site')
    site_url = models.CharField(max_length=200, verbose_name='Domain site')
    address = models.CharField(max_length=200, verbose_name='Address')
    phone = models.CharField(max_length=200, null=True, blank=True, verbose_name='Phone')
    fax = models.CharField(max_length=200, null=True, blank=True, verbose_name='fax')
    email = models.CharField(max_length=200, null=True, blank=True, verbose_name='email')
    copy_right = models.TextField(verbose_name='Text copy right site')
    about_us_text = models.TextField(verbose_name='Text in With our site')
    site_logo = models.ImageField(upload_to='images/site-setting/', verbose_name='logo site')
    is_main_setting = models.BooleanField(verbose_name='Settings Main')

    class Meta:
        verbose_name = 'Settings site'
        verbose_name_plural = 'Settings'

    def __str__(self):
        return self.site_name


class FooterLinkBox(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')

    class Meta:
        verbose_name = 'Category footer links'
        verbose_name_plural = 'Categories of footer links'

    def __str__(self):
        return self.title


class FooterLink(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')
    url = models.URLField(max_length=500, verbose_name='link')
    footer_link_box = models.ForeignKey(to=FooterLinkBox, on_delete=models.CASCADE, verbose_name='Category')

    class Meta:
        verbose_name = 'link footer'
        verbose_name_plural = 'link footer'

    def __str__(self):
        return self.title


class Slider(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')
    url = models.URLField(max_length=500, verbose_name='link')
    url_title = models.CharField(max_length=200, verbose_name='Title link')
    description = models.TextField(verbose_name='description slidein')
    image = models.ImageField(upload_to='images/sliders', verbose_name='Image slide-in')
    is_active = models.BooleanField(default=True, verbose_name='active / Inactive')

    class Meta:
        verbose_name = 'slide in'
        verbose_name_plural = 'slide ins'

    def __str__(self):
        return self.title


class SiteBanner(models.Model):
    class SiteBannerPositions(models.TextChoices):
        product_list = 'product_list', 'Page list Products',
        product_detail = 'product_detail', 'Product details page',
        about_us = 'about_us', 'inWith us'

    title = models.CharField(max_length=200, verbose_name='Title banner')
    url = models.URLField(max_length=400, null=True, blank=True, verbose_name='Address banner')
    image = models.ImageField(upload_to='images/banners', verbose_name='Image banner')
    is_active = models.BooleanField(verbose_name='active / Inactive')
    position = models.CharField(max_length=200, choices=SiteBannerPositions.choices, verbose_name='show place')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'banner Promotional'
        verbose_name_plural = 'Banners Promotional'
