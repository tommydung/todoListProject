# Generated by Django 3.1.1 on 2020-09-28 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0007_auto_20200927_0120'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=100, upload_to='cars'),
            preserve_default=False,
        ),
    ]
