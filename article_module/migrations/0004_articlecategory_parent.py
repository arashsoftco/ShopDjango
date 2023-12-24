# Generated by Django 3.2.11 on 2022-02-25 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article_module', '0003_alter_articlecategory_url_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlecategory',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='article_module.articlecategory', verbose_name='Category parent'),
        ),
    ]