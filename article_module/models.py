from django.db import models
from jalali_date import date2jalali
from account_module.models import User


class ArticleCategory(models.Model):
    parent = models.ForeignKey('ArticleCategory', null=True, blank=True, on_delete=models.CASCADE, verbose_name='Category parent')
    title = models.CharField(max_length=200, verbose_name='Title Category')
    url_title = models.CharField(max_length=200, unique=True, verbose_name='Title in url')
    is_active = models.BooleanField(default=True, verbose_name='active / Inactive')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category Article'
        verbose_name_plural = 'Category of Article'


class Article(models.Model):
    title = models.CharField(max_length=300, verbose_name='Title Article')
    slug = models.SlugField(max_length=400, db_index=True, allow_unicode=True, verbose_name='Title in url')
    image = models.ImageField(upload_to='images/articles', verbose_name='Image Article')
    short_description = models.TextField(verbose_name='Short description')
    text = models.TextField(verbose_name='Text Article')
    is_active = models.BooleanField(default=True, verbose_name='active / Inactive')
    selected_categories = models.ManyToManyField(ArticleCategory, verbose_name='Category ')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='writer', null=True, editable=False)
    create_date = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Date of Registration')

    def __str__(self):
        return self.title

    def get_jalali_create_date(self):
        return date2jalali(self.create_date)

    def get_jalali_create_time(self):
        return self.create_date.strftime('%H:%M')

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'articles'


class ArticleComment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Article')
    parent = models.ForeignKey('ArticleComment', null=True, blank=True, on_delete=models.CASCADE, verbose_name='parent')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='user')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Date of Registration')
    text = models.TextField(verbose_name='Text Opinion')

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'Opinion Article'
        verbose_name_plural = 'Comments Article'
