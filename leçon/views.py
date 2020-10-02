from django.shortcuts import render,redirect
from .forms import LessonForm,VideoForm
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
    form = LessonForm(instance=lesson)
    if request.method == 'POST' and 'LessonForm' in request.POST:
        form = LessonForm(request.POST,instance=lesson)
        if form.is_valid:
            form.save()
            return redirect('lesson_info',lesson.id)
    context={
        'lesson':lesson,
        'form':form,
        }

    return render(request,'leçon/lesson_info.html',context)

def add_lesson_video(request,lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    return render(request,'leçon/add_lesson_video.html')
