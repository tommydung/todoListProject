# Generated by Django 3.1.1 on 2020-09-27 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0004_auto_20200926_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
