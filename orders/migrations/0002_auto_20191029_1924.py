# Generated by Django 2.2.1 on 2019-10-29 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_first_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='order_last_name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
