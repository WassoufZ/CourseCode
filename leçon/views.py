from django.shortcuts import render,redirect,HttpResponseRedirect
from .forms import LessonForm,VideoForm,ImageForm
from.models import *


# Create your views here.
def view_lessons(request):
    lessons = Lesson.objects.all()
    context={
        'lessons':lessons,
    }
    return render(request,'leçon/view_lessons.html',context)

def add_lesson(request):
    form = LessonForm
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('view_lessons')
    context = {
        'form':form,
    }
    return render(request,'leçon/add_lesson.html',context)


def delete_lesson(request,pk):
    lesson = Lesson.objects.get(pk=pk)
    lesson.delete()
    return redirect('view_lessons')

def lesson_info(request,pk):
    lesson = Lesson.objects.get(pk=pk)
    videos = Video.objects.filter(lesson=lesson)
    images = Image.objects.filter(lesson=lesson)

    form = LessonForm(instance=lesson)
    if request.method == 'POST' and 'LessonForm' in request.POST:
        form = LessonForm(request.POST,instance=lesson)
        if form.is_valid:
            form.save()
            return redirect('lesson_info',lesson.id)
    context={
        'lesson':lesson,
        'form':form,
        'videos':videos,
        'images':images,
        }

    return render(request,'leçon/lesson_info.html',context)


def add_lesson_video(request,lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    form = VideoForm
    if request.method == 'POST':
        form = VideoForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.lesson = lesson
            instance.save()
            return redirect('lesson_info',lesson_id)
    context = {
        'form':form,
        'lesson':lesson,
    }
    return render(request,'leçon/add_lesson_video.html',context)

def edit_lesson_video(request,lesson_id,pk):
    lesson = Lesson.objects.get(id=lesson_id)
    video = Video.objects.get(pk=pk)
    form = VideoForm(instance=video)
    if request.method == 'POST':
        form = VideoForm(request.POST,request.FILES,instance=video)
        if form.is_valid():
            form.save()
            return redirect('lesson_info',lesson_id)
    context = {
        'form':form,
        'lesson':lesson,
    }
    return render(request,'leçon/add_lesson_video.html',context)

def delete_lesson_video(request,pk):
    video = Video.objects.get(pk=pk)
    video.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def add_lesson_image(request,lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    form = ImageForm
    if request.method == 'POST':
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.lesson = lesson
            instance.save()
            return redirect('lesson_info',lesson_id)
    context = {
        'form':form,
        'lesson':lesson,
    }
    return render(request,'leçon/add_lesson_image.html',context)


def edit_lesson_image(request,lesson_id,pk):
    lesson = Lesson.objects.get(id=lesson_id)
    image = Image.objects.get(pk=pk)
    form = ImageForm(instance=image)
    if request.method == 'POST':
        form = ImageForm(request.POST,request.FILES,instance=image)
        if form.is_valid():
            form.save()
            return redirect('lesson_info',lesson_id)
    context = {
        'form':form,
        'lesson':lesson,
    }
    return render(request,'leçon/add_lesson_image.html',context)

def delete_lesson_image(request,pk):
    image = Image.objects.get(pk=pk)
    image.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))





    '''
    lesson = Lesson.objects.get(id=lesson_id)
    form = ImageForm
    if request.method == 'POST':
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.lesson = lesson
            instance.save()
            return redirect('lesson_info',lesson_id)
    context = {
        'form':form,
        'lesson':lesson,
    }
    return render(request,'leçon/add_lesson_image.html',context)'''