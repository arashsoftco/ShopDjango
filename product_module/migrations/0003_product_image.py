# Generated by Django 3.2.11 on 2022-01-25 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0002_auto_20211220_2231'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/products', verbose_name='Image product'),
        ),
    ]