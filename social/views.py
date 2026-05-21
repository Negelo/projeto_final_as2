from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render

from .models import Comment, Like, Post


def home(request):
    posts = Post.objects.select_related("author").annotate(
        like_count=Count("likes"),
        comment_count=Count("comments"),
    )
    return render(request, "social/home.html", {"posts": posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post.objects.select_related("author"), id=post_id)

    if request.method == "POST":
        if "like" in request.POST and request.user.is_authenticated:
            Like.objects.get_or_create(post=post, user=request.user)
            return redirect("post_detail", post_id=post.id)

        if "comment" in request.POST and request.user.is_authenticated:
            content = request.POST.get("content", "").strip()
            if content:
                Comment.objects.create(post=post, author=request.user, content=content)
            return redirect("post_detail", post_id=post.id)

    comments = post.comments.select_related("author")
    context = {
        "post": post,
        "comments": comments,
        "like_count": post.likes.count(),
        "comment_count": comments.count(),
    }
    return render(request, "social/post_detail.html", context)


def user_posts(request, username):
    posts = Post.objects.select_related("author").filter(author__username=username)
    context = {
        "username": username,
        "posts": posts,
    }
    return render(request, "social/user_posts.html", context)
