# Generated by Django 3.2.12 on 2022-04-17 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0006_sitebanners'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title banner')),
                ('url', models.URLField(blank=True, max_length=400, null=True, verbose_name='Address banner')),
                ('image', models.ImageField(upload_to='images/banners', verbose_name='Image banner')),
                ('is_active', models.BooleanField(verbose_name='active / Inactive')),
                ('position', models.CharField(choices=[('product_list', 'Page list Products'), ('product_detail', 'Product details page'), ('about_us', 'inWith us')], max_length=200, verbose_name='show place')),
            ],
            options={
                'verbose_name': 'banner Promotional',
                'verbose_name_plural': 'banner Promotional',
            },
        ),
        migrations.DeleteModel(
            name='SiteBanners',
        ),
    ]