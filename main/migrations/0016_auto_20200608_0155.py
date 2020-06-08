# Generated by Django 2.2.10 on 2020-06-08 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_category_brands'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='slug',
            new_name='category_slug',
        ),
        migrations.AlterField(
            model_name='category',
            name='brands',
            field=models.ManyToManyField(blank=True, to='main.Brand'),
        ),
    ]
