from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse,reverse
from django.core.files.storage import FileSystemStorage
from django.views.generic import ListView
from django.db.models import Q
from .forms import *
from.models import *
from pathlib import Path
from django.core.exceptions import ValidationError
from django.contrib import messages




#===========================lesson section=====================

def view_lessons_list(request):
    lessons = Lesson.objects.all()
    context={
        'lessons':lessons,
    }
    return render(request,'leçon/view_lessons_list.html',context)

def view_lessons_videos(request):
    videos = Video.objects.all()
    context={
        'videos':videos,
    }
    return render(request,'leçon/view_lessons_videos.html',context)

class SearchView(ListView):
    model = Lesson
    template_name = 'leçon/search_view.html'
    def get_queryset(self):
        word = self.request.GET.get('q')
        object_list = Lesson.objects.filter(Q(chapiter__icontains=word)|Q(lesson__icontains=word))
        return object_list

def view_lesson(request,pk):
    lesson = Lesson.objects.get(pk=pk)
    videos = Video.objects.filter(lesson=lesson)
    images = Image.objects.filter(lesson=lesson)
    documents = Document.objects.filter(lesson=lesson)
    urls = Url.objects.filter(lesson=lesson)
    context={
        'lesson':lesson,
        'videos':videos,
        'images':images,
        'documents':documents,
        'urls':urls,
        }
    return render(request,'leçon/view_lesson.html',context)


def edit_lesson(request,pk):
    lesson = Lesson.objects.get(pk=pk)
    videos = Video.objects.filter(lesson=lesson)
    images = Image.objects.filter(lesson=lesson)
    documents = Document.objects.filter(lesson=lesson)
    urls = Url.objects.filter(lesson=lesson)


    form = LessonForm(instance=lesson)
    form1 = UrlForm


    if request.method == 'POST' and 'LessonForm' in request.POST:
        form = LessonForm(request.POST,instance=lesson)
        if form.is_valid:
            form.save()
            return redirect('edit_lesson',lesson.id)

    if request.method == 'POST' and 'UrlForm' in request.POST:
        form = UrlForm(request.POST)
        if form.is_valid:
            instance = form.save(commit=False)
            instance.lesson = lesson
            instance.save()
            messages.success(request, "Url a été enregistrées.")
            return redirect('edit_lesson',lesson.id)
    context={
        'lesson':lesson,
        'form':form,
        'form1':form1,
        'videos':videos,
        'images':images,
        'documents':documents,
        'urls':urls,
        }
    return render(request,'leçon/edit_lesson.html',context)


def add_lesson(request):
    form = LessonForm
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid:
            new_lesson = form.save()
            return HttpResponseRedirect(reverse(edit_lesson, args=(new_lesson.pk,)))
    context = {
        'form':form,
    }
    return render(request,'leçon/add_lesson.html',context)


def delete_lesson(request,pk):
    lesson = Lesson.objects.get(pk=pk)
    lesson.delete()
    return redirect('view_lessons_list')

#==============================lesson videos section=================

def add_lesson_video(request,lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    form = VideoForm
    if request.method == 'POST':
        form = VideoForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.lesson = lesson
            instance.save()
            return redirect('edit_lesson',lesson_id)
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
            return redirect('edit_lesson',lesson_id)
    context = {
        'form':form,
        'lesson':lesson,
    }
    return render(request,'leçon/add_lesson_video.html',context)

def delete_lesson_video(request,pk):
    video = Video.objects.get(pk=pk)
    video.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))



#==========================lesson images section=========================

def add_lesson_image(request,lesson_id):
    if request.method == 'POST':
        lesson = Lesson.objects.get(id=lesson_id)
        title = request.POST.get('title')
        images = request.FILES.getlist("file[]")
        allowed = ['.jpg','.png','jpeg']            #list of the allowed images formats
        valid = []
        for img in images:
            if Path(str(img)).suffix in allowed:    #filtering the images by valid formats
                valid.append(img)
            else:
                messages.warning(request, f"l'extension de fichier '{img}' et n'est pas autorisée")
        for img in valid:                           #saving images one by one
            fs = FileSystemStorage()
            file_path=fs.save(img.name,img)
            image=Image(lesson=lesson,title=title,image=file_path)
            image.save()
        if len(valid) > 0:                          #checking if the user input has valid images
            messages.success(request, "Les images a été enregistrées.")
        else: 
            messages.success(request, "aucune image ajoutée")
        return redirect('edit_lesson',lesson_id)

    return render (request,'leçon/add_lesson_image.html')


def edit_lesson_image(request,lesson_id,pk):
    lesson = Lesson.objects.get(id=lesson_id)
    image = Image.objects.get(pk=pk)
    form = ImageForm(instance=image)
    if request.method == 'POST':
        form = ImageForm(request.POST,request.FILES,instance=image)
        if form.is_valid():
            form.save()
            return redirect('edit_lesson',lesson_id)
    context = {
    'form':form,
    'lesson':lesson,
    'image':image,
   }
    return render(request,'leçon/edit_lesson_image.html',context)


def delete_lesson_image(request,pk):
    image = Image.objects.get(pk=pk)
    image.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


#==========================lesson documents section=========================

def add_lesson_document(request,lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    form = DocumentForm()
    if request.method == 'POST':
        form = DocumentForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.lesson = lesson
            instance.save()

            messages.success(request, "Le document a été enregistrées.")
            return redirect('edit_lesson',lesson_id)
    context = {
    'form':form,
    'lesson':lesson,
   }
    return render(request,'leçon/add_lesson_document.html',context)

def edit_lesson_document(request,lesson_id,pk):
    lesson = Lesson.objects.get(id=lesson_id)
    document = Document.objects.get(pk=pk)
    form = DocumentForm(instance=document)
    if request.method == 'POST':
        form = DocumentForm(request.POST,request.FILES,instance=document)
        if form.is_valid():
            form.save()
            return redirect('edit_lesson',lesson_id)
    context = {
    'form':form,
    'lesson':lesson,
   }
    return render(request,'leçon/add_lesson_document.html',context)


def delete_lesson_document(request,pk):
    document = Document.objects.get(pk=pk)
    document.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

#==========================lesson documents delete=========================
def delete_lesson_url(request,pk):
    url = Url.objects.get(pk=pk)
    url.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))



