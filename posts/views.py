"""Posts Views"""

# Django
from django.shortcuts import render, redirect
from django.views.generic import ListView
# from django.http import HttpResponse

# Models
from posts.models import Post

# Forms
from posts.forms import PostForm


def create_post(request):
    """Create new post view"""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:feed')
    else:
        form = PostForm()
    
    return render(request, 'posts/new.html', {'form':form})


class PostFeedView(ListView):
    """Return all published posts."""
    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 2
    context_object_name = 'posts'
