# Generated by Django 2.2.1 on 2019-09-10 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_book_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(help_text='A slug is a short label, used in URLs'),
        ),
    ]