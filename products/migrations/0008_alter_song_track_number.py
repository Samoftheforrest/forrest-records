# Generated by Django 3.2 on 2022-09-23 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_song_track_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='track_number',
            field=models.CharField(default='1', max_length=3),
            preserve_default=False,
        ),
    ]
