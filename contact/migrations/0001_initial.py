# Generated by Django 3.2 on 2022-09-21 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=16)),
                ('subtitle', models.CharField(max_length=16)),
            ],
            options={
                'verbose_name_plural': 'Contact Page',
            },
        ),
    ]
