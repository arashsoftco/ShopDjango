from django.db import models
from django.urls import reverse
from account_module.models import User


# Create your models here.

class ProductCategory(models.Model):
    title = models.CharField(max_length=300, db_index=True, verbose_name='Title')
    url_title = models.CharField(max_length=300, db_index=True, verbose_name='Title in url')
    is_active = models.BooleanField(verbose_name='active / Inactive')
    is_delete = models.BooleanField(verbose_name='Deleted/ not done')

    def __str__(self):
        return f'( {self.title} - {self.url_title} )'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Category '


class ProductBrand(models.Model):
    title = models.CharField(max_length=300, verbose_name='name brand', db_index=True)
    url_title = models.CharField(max_length=300, verbose_name='name in url', db_index=True)
    is_active = models.BooleanField(verbose_name='active / Inactive')

    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'brand '

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=300, verbose_name='name product')
    category = models.ManyToManyField(ProductCategory, related_name='product_categories', verbose_name='Category ')
    image = models.ImageField(upload_to='images/products', null=True, blank=True, verbose_name='Image product')
    brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE, verbose_name='brand', null=True, blank=True)
    price = models.IntegerField(verbose_name='Price')
    short_description = models.CharField(max_length=360, db_index=True, null=True, verbose_name='Short description')
    description = models.TextField(verbose_name='descriptionMain', db_index=True)
    slug = models.SlugField(default="", null=False, db_index=True, blank=True, max_length=200, unique=True, verbose_name='Title in url')
    is_active = models.BooleanField(default=False, verbose_name='active / Inactive')
    is_delete = models.BooleanField(verbose_name='Deleted/ not done')

    def get_absolute_url(self):
        return reverse('product-detail', args=[self.slug])

    def save(self, *args, **kwargs):
        # self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.price})"

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'product'


class ProductTag(models.Model):
    caption = models.CharField(max_length=300, db_index=True, verbose_name='Title')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_tags')

    class Meta:
        verbose_name ='product tag'
        verbose_name_plural = "Product Tags"

    def __str__(self):
        return self.caption


class ProductVisit(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='product')
    ip = models.CharField(max_length=30, verbose_name='IP user')
    user = models.ForeignKey(User, null=True, blank=True, verbose_name='user', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product.title} / {self.ip}'

    class Meta:
        verbose_name = 'With new product'
        verbose_name_plural = 'With product updates'


class ProductGallery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='product')
    image = models.ImageField(upload_to='images/product-gallery', verbose_name='Image')

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = 'Image gallery'
        verbose_name_plural = 'gallery gallery'
