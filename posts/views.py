from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostCreateForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# Create your views here.

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            return redirect('index')
    else:
        form = PostCreateForm()
    return render(request, 'posts/create.html', {'form': form})


def feed(request):
    posts = Post.objects.all()
    comment_form = CommentForm()
    return render(request, 'posts/feed.html', {'posts': posts, 'comment_form': comment_form})


def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'posts/detail.html', {'post': post})

def like_post(request):
    post_id = request.POST.get('post_id')
    post = get_object_or_404(Post, id=post_id)
    if post.liked_by.filter(id=request.user.id).exists():
        post.liked_by.remove(request.user)
    else:
        post.liked_by.add(request.user)
    post.save()
    return JsonResponse({'status': 'success'})

@login_required
def add_comment(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        post_id = request.POST.get('post_id')
        comment_body = request.POST.get('body')
        posted_by = request.POST.get('posted_by')
        if not comment_body or not comment_body.strip():
            return JsonResponse({'success': False, 'message': 'Comment cannot be empty.'})

        try:
            post = get_object_or_404(Post, id=post_id)
            comment = Comment(post=post, body=comment_body, posted_by=posted_by)
            comment.save()
            return JsonResponse({'success': True, 'comment_author': posted_by, 'comment_body': comment_body})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    return JsonResponse({'success': False, 'message': 'Invalid request'})