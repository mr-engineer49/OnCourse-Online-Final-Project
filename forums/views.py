from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required

from forums.forms import ForumCreateForm, ThreadCreateForm
from .models import Forum, Thread, Post


def forum_list(request):
    forums = Forum.objects.select_related('course').order_by('course__title')
    threads = Thread.objects.all()
    # Check if the user is authenticated first
    if request.user.is_authenticated:
        is_instructor = request.user.is_instructor
        is_institution = request.user.is_institution
        is_learner = request.user.is_learner
    else:
        # If the user is not authenticated, set these variables to False
        is_instructor = False
        is_institution = False
        is_learner = False
    context={
        'forums': forums,
        'is_instructor': is_instructor,
        'is_institution': is_institution,
        'is_learner': is_learner,
        'threads': threads
    }
    return render(request, 'forums/forum_page.html', context)


def forum_detail(request, course_pk):
    forum = Forum.objects.filter(course=course_pk)
    threads = Thread.objects.filter(forum=forum)
    return render(request, 'forums/forum_page.html', {'forum': forum, 'threads': threads})

def thread_detail(request, forum_pk, thread_pk):
    forum = get_object_or_404(Forum, pk=forum_pk)
    thread = get_object_or_404(Thread, pk=thread_pk, forum=forum)
    posts = Post.objects.filter(thread=thread)
    return render(request, 'forums/thread_detail.html', {'thread': thread, 'posts': posts})



def thread_create(request):    
    if request.method == 'POST':
        thread_form = ThreadCreateForm(request.POST)
        if thread_form.is_valid():
            thread = thread_form.save(commit=False)
            thread.save()
            return redirect('forums:forum_list')
        else:
            print(thread_form.errors)
    else:
        thread_form = ThreadCreateForm()
    
    return render(request, 'forums/thread_form.html', {'thread_form': thread_form})



def forum_create(request):
    if request.method == 'POST':
        forum_form = ForumCreateForm(request.POST)
        if forum_form.is_valid():
            forum = forum_form.save(commit=False)
            forum.save()
            return redirect('forums:forum_list')
        else:
            print(forum_form.errors)
    else:
        forum_form = ForumCreateForm()

    return render(request, 'forums/forum_form.html', {'forum_form': forum_form})







