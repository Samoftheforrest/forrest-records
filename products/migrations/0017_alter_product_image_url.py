# Generated by Django 3.2 on 2022-10-08 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_url',
            field=models.URLField(blank=True, help_text='If you have your image hosted anywhere else, add the link here to server as a backup.', max_length=1024, null=True),
        ),
    ]
