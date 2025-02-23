from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm
from .models import Post
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from django.shortcuts import get_object_or_404

@login_required
def profile(request):
    user_posts = Post.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'posts/profile.html', {'posts': user_posts})
def homepage(request):
    posts = Post.objects.all().order_by('-created_at')

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

    return render(request, 'posts/homepage.html', {'posts': posts, 'form': form})
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
