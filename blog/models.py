import datetime
from ckeditor.fields import RichTextField
from django.conf import settings
from django.db import models
from profiles.models import UserProfile


class Blog(models.Model):
    """
    Model for individual blogs.
    """

    title = models.CharField(
        max_length=254,
        null=False,
        blank=False)

    author = models.ForeignKey(
        UserProfile,
        null=True,
        blank=True,
        on_delete=models.SET_NULL)

    content = RichTextField()

    image = models.ImageField(
        upload_to='images/',
        null=True,
        blank=True,
    )

    image_url = models.CharField(
        max_length=254,
        null=True,
        blank=True,
        help_text='If you have your image hosted anywhere else, add the link here to server as a backup.'
    )

    date_published = models.DateField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title


class BlogPage(models.Model):
    """
    Model for blog page.
    """
    class Meta:
        """
        Model admin settings.
        """
        verbose_name_plural = 'Blog Page'

    title = models.CharField(
        max_length=16,
        null=False,
        blank=False)

    subtitle = models.CharField(
        max_length=64,
        null=False,
        blank=False)

    featured_blog = models.ForeignKey(
        Blog,
        null=True,
        blank=True,
        on_delete=models.SET_NULL)

    def __str__(self):
        return 'Blog page'
