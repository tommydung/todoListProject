# Generated by Django 3.1.1 on 2020-09-29 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0009_auto_20200928_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='/media/static/images/dogs.png', upload_to='static/images'),
        ),
    ]
