from .forms import RegistrationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q  # <-- Import this
from .models import Post
from .forms import PostForm


@login_required
def profile(request):
    user_posts = Post.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'posts/profile.html', {'posts': user_posts})

def homepage(request):
    # Get all posts ordered by latest first
    posts = Post.objects.all().order_by('-created_at')

    # Filtering & Search Logic
    # Date Filter
    date_filter = request.GET.get('date')
    if date_filter == 'latest':
        posts = posts.order_by('-created_at')
    elif date_filter == 'oldest':
        posts = posts.order_by('created_at')

    # Media Filter
    media_filter = request.GET.get('media')
    if media_filter == 'text':
        posts = posts.filter(image__isnull=True)
        print(f"Text Only Posts: {posts.query}")
    elif media_filter == 'images':
        posts = posts.filter(image__isnull=False)

    # Author Filter
    author_filter = request.GET.get('author')
    if author_filter:
        posts = posts.filter(author__username=author_filter)

    # Keyword Search
    keyword = request.GET.get('search')
    if keyword:
        posts = posts.filter(Q(content__icontains=keyword) | Q(author__username__icontains=keyword))

    # Post Creation Logic
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            messages.success(request, 'Post created successfully!')
            return redirect('homepage')
    else:
        form = PostForm()

    context = {
        'posts': posts,
        'form': form,
        'date_filter': date_filter,
        'media_filter': media_filter,
        'author_filter': author_filter,
        'keyword': keyword,
    }

    return render(request, 'posts/homepage.html', context)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. You can now log in.')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'posts/register.html', {'form': form})

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)  # Ensure the user is the author

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)  # Pre-fill form with existing post data
        if form.is_valid():
            form.save()
            return redirect('homepage')  # Redirect to homepage after updating
    else:
        form = PostForm(instance=post)  # Display form pre-filled with the existing post data

    return render(request, 'posts/edit_post.html', {'form': form})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)  # Ensure the user is the author

    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Your post has been deleted successfully.')
        return redirect('homepage')  # Redirect to homepage after deletion

    return render(request, 'posts/confirm_delete.html', {'post': post})
