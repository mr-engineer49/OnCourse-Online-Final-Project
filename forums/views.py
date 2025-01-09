from django.shortcuts import render, get_object_or_404
from .models import Forum, Thread, Post


def forum_list(request):
    forums = Forum.objects.all()
    threads = Thread.objects.all()
    return render(request, 'forums/forum_page.html', {'forums': forums, 'threads': threads})

def forum_detail(request, course_pk):
    forum = Forum.objects.filter(course=course_pk)
    threads = Thread.objects.filter(forum=forum)
    return render(request, 'forums/forum_page.html', {'forum': forum, 'threads': threads})



def thread_detail(request, forum_pk, thread_pk):
    forum = get_object_or_404(Forum, pk=forum_pk)
    thread = get_object_or_404(Thread, pk=thread_pk, forum=forum)
    posts = Post.objects.filter(thread=thread)
    return render(request, 'forums/thread_detail.html', {'thread': thread, 'posts': posts})