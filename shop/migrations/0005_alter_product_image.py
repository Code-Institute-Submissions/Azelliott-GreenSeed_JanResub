# Generated by Django 4.1.3 on 2022-12-28 20:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='default/not-found.jpeg', null=True, upload_to='products', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg']), django.core.validators.MinLengthValidator(1024)]),
        ),
    ]