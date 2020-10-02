from django.shortcuts import render,redirect
from .forms import LessonForm
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