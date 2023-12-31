# Generated by Django 3.2.7 on 2021-12-04 04:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('price', models.IntegerField(verbose_name='Price')),
                ('short_description', models.CharField(db_index=True, max_length=360, null=True, verbose_name='Short description')),
                ('description', models.TextField(db_index=True, verbose_name='descriptionMain')),
                ('slug', models.SlugField(blank=True, default='', max_length=200, unique=True)),
                ('is_active', models.BooleanField(default=False, verbose_name='active / Inactive')),
                ('is_delete', models.BooleanField(verbose_name='Deleted/ not done')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=300, verbose_name='Title')),
                ('url_title', models.CharField(db_index=True, max_length=300, verbose_name='Title in url')),
                ('is_active', models.BooleanField(verbose_name='active / Inactive')),
                ('is_delete', models.BooleanField(verbose_name='Deleted/ not done')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='ProductTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(db_index=True, max_length=300, verbose_name='Title')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_tags', to='product_module.product')),
            ],
            options={
                'verbose_name': 'tag product',
                'verbose_name_plural': 'tag  Products',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(related_name='product_categories', to='product_module.ProductCategory', verbose_name='Category'),
        ),
    ]
