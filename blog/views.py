from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import BlogPage, Blog
from .forms import BlogForm


def all_blog_posts(request):
    """
    Returns all blog posts, including sorting
    """
    blog_page = BlogPage.objects.all()
    blogs = Blog.objects.all().order_by('blogpage__featured_blog', '-id')
    featured_blog = None

    for item in blog_page:
        if item.featured_blog:
            featured_blog = item.featured_blog

    context = {
        'blog_page': blog_page,
        'blogs': blogs,
        'featured_blog': featured_blog,
    }

    return render(request, 'blog/blog.html', context)


def blog_detail(request, blog_id):
    """
    Redirects to a specific blog page
    """
    blog = get_object_or_404(Blog, id=blog_id)
    blog_title = blog.title
    modifier = '__blogsingle'

    context = {
        'modifier': modifier,
        'blog': blog,
        'blog_title': blog_title,
    }

    return render(request, 'blog/blog-single.html', context)


@login_required
def add_blog(request):
    """
    Add a new blog post
    """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('blog')) 

    page_title = 'Add a Blog Post'

    if request.method == 'POST':

        # Form validation - extra check to ensure no required fields are empty
        title = request.POST['title']
        if not title:
            messages.error(request, 'Please ensure your blog has a title.')
            return redirect(reverse('add_blog'))

        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save()
            messages.success(request, 'Successfully added blog post!')
            return redirect(reverse('blog_detail', args=[blog.id]))
        else:
            messages.error(request, 'Failed to add blog post.')
    else:
        form = BlogForm()

    template = 'blog/add-blog.html'
    context = {
        'page_title': page_title,
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_blog(request, blog_id):
    """
    Edit a blog.
    """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('blog'))

    page_title = 'Edit Blog Post'
    blog = get_object_or_404(Blog, pk=blog_id)

    if request.method == 'POST':

        # Form validation - extra check to ensure no required fields are empty
        title = request.POST['title']
        if not title:
            messages.error(request, 'Please ensure your blog has a title.')
            return redirect(reverse('edit_blog', args=[blog.id]))
        
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully edited {blog.title}')
            return redirect(reverse('blog_detail', args=[blog.id]))
        else:
            messages.error(request, f'Failed to edit {blog.title}.')
    else:
        form = BlogForm(instance=blog)
        messages.info(request, f'You are editing {blog.title}')

    template = 'blog/edit-blog.html'
    context = {
        'page_title': page_title,
        'form': form,
        'blog': blog
    }

    return render(request, template, context)


@login_required
def blog_warning(request, blog_id):
    """
    Renders the warning page when a store owner tries to delete a blog
    """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('blog'))
    
    page_title = 'Warning!'
    blog = get_object_or_404(Blog, pk=blog_id)
    template = 'includes/warning/warning.html'
    context = {
        'page_title': page_title,
        'blog': blog,
    }

    return render(request, template, context)


@login_required
def delete_blog(request, blog_id):
    """
    Delete blog post
    """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('blog'))

    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()
    messages.success(request, f'{blog.title} has been deleted!')
    return redirect(reverse('blog'))


@login_required
def feature_blog(request, blog_id):
    """
    Sets a blog posts' status to featured
    """
    if not request.user.is_staff:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('blog'))

    blog_page = BlogPage.objects.get(pk=1)

    if blog_id == 'None':
        blog_page.featured_blog = None
        blog_page.save()
        return redirect(reverse('blog'))

    blog = get_object_or_404(Blog, pk=blog_id)
    blog_page = BlogPage.objects.get(pk=1)
    blog_page.featured_blog = blog

    blog_page.save()

    return redirect(reverse('blog'))
