from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_blog_posts, name='blog'),
    path('<blog_id>', views.blog_detail, name='blog_detail'),
]
