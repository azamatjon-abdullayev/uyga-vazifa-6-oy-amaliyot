from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_object_or_404, get_list_or_404

from .models import *
# Create your views here.

def index(request: WSGIRequest):
    posts = Lesson.objects.filter(published=True)
    context = {
        "posts": posts,
        "title": "Barcha maqolalar"
    }
    return render(request, "index.html", context)


def posts_by_category(request, category_id):
    posts = get_list_or_404(Lesson, category_id=category_id, published=True)
    category = get_object_or_404(Lesson, pk=category_id)
    context = {
        'posts': posts,

    }
    return render(request, 'index.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Lesson, pk=post_id, published=True)
    post.views += 1
    post.save()

    context = {
        "post": post,
        "title": post.title
    }
    return render(request, 'detail.html', context)

