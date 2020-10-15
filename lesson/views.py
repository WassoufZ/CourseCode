from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse,reverse
from django.core.files.storage import FileSystemStorage
from django.views.generic import ListView
from django.db.models import Q
from .forms import *
from .models import *
from scolarité.models.level import Level
from scolarité.models.subject import Subject
from pathlib import Path
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.contrib.auth.decorators import login_required



#=========================== view lessons =====================
@login_required  #use this to make the view accessible for logged in users only
def view_lessons_list(request,subject_id):
    request.session['subject_id']= subject_id                       #assign subject id value to session
    level = Level.objects.get(id=request.session['level_id'])       #getting the level model 
    subject = Subject.objects.get(id=request.session['subject_id']) #getting the subject model 
    lessons = Lesson.objects.filter(subject=subject ,level=level).order_by('order')  #filtering the lesson based on the chosen level and subject
    context={'lessons':lessons,}
    return render(request,'lesson/view_lessons_list.html',context)


class VideosView(ListView):
    model = Video
    template_name = 'lesson/view_lessons_videos.html'
    def get_queryset(self):
        level = Level.objects.get(id=self.request.session['level_id'])
        subject = Subject.objects.get(id=self.request.session['subject_id'])
        lessons = Lesson.objects.filter(subject=subject ,level=level)
        object_list = Video.objects.filter(lesson__in=lessons)      #filtering the videos that has the same lasson object
        return object_list

def view_video(request,pk):
    '''if request.user.user_type == 'school_admin':
        pass
    else:'''
    video = Video.objects.get(pk=pk)
    video.views += 1
    video.save()
    return render(request,'lesson/view_video.html',{'video':video})

class ImagesView(ListView):
    model = Image
    template_name = 'lesson/view_lessons_images.html'
    def get_queryset(self):
        level = Level.objects.get(id=self.request.session['level_id'])
        subject = Subject.objects.get(id=self.request.session['subject_id'])
        lessons = Lesson.objects.filter(subject=subject ,level=level)
        object_list = Image.objects.filter(lesson__in=lessons)      
        return object_list
def ajax_image_views(request,pk):
    '''if request.user.user_type == 'school_admin':
        pass
    else:'''
    image = Image.objects.get(pk=pk)
    image.views += 1
    image.save() 
    return HttpResponse('done')

class DocumentsView(ListView):
    model = Document
    template_name = 'lesson/view_lessons_documents.html'
    def get_queryset(self):
        level = Level.objects.get(id=self.request.session['level_id'])
        subject = Subject.objects.get(id=self.request.session['subject_id'])
        lessons = Lesson.objects.filter(subject=subject ,level=level)
        object_list = Document.objects.filter(lesson__in=lessons)      
        return object_list
def ajax_document_views(request,pk):
    '''if request.user.user_type == 'school_admin':
        pass
    else:'''
    document = Document.objects.get(pk=pk)
    document.views += 1
    document.save() 
    return HttpResponse('done')

def ajax_url_views(request,pk):
    '''if request.user.user_type == 'school_admin':
        pass
    else:'''
    url = Url.objects.get(pk=pk)
    url.views += 1
    url.save() 
    return HttpResponse('done')


class SearchView(ListView):
    model = Lesson
    template_name = 'lesson/search_view.html'
    def get_queryset(self):
        level = Level.objects.get(id=self.request.session['level_id'])
        subject = Subject.objects.get(id=self.request.session['subject_id'])

        word = self.request.GET.get('q')                            #q is the name of the input field in the search form
        result = Lesson.objects.filter(Q(chapiter__icontains=word)|Q(lesson__icontains=word))#search result based on chapiter or/and lesson
        object_list = result.filter(level=level,subject=subject) #filtering the lessons list that has the same word as 'q'
        return object_list


def view_lesson(request,pk):
    lesson = Lesson.objects.get(pk=pk)
    videos = Video.objects.filter(lesson=lesson)
    images = Image.objects.filter(lesson=lesson)
    documents = Document.objects.filter(lesson=lesson)
    urls = Url.objects.filter(lesson=lesson)
    #add this if statment to count views only from students
    '''if request.user.user_type == 'school_admin':
        pass
    else:'''
    lesson.views = lesson.views + 1
    lesson.save()
    context={
        'lesson':lesson,
        'videos':videos,
        'images':images,
        'documents':documents,
        'urls':urls,
        }
    return render(request,'lesson/view_lesson.html',context)


#========================add/edit/remove lesson section==========================
def add_lesson(request):
    level = Level.objects.get(id=request.session['level_id'])
    subject = Subject.objects.get(id=request.session['subject_id'])

    form = LessonForm
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid:
            instance = form.save(commit=False)
            instance.level = level
            instance.subject = subject
            instance.save()
            messages.success(request, "leçon a été créée avec succès, ajoutez les fichiers multimédias de votre leçon maintenant.")
            return HttpResponseRedirect(reverse(edit_lesson, args=[instance.id] ))#redirecting to the edit lesson page 
    context = {
        'form':form,
    }
    return render(request,'lesson/add_lesson.html',context)


def edit_lesson(request,pk):
    lesson = Lesson.objects.get(pk=pk)
    videos = Video.objects.filter(lesson=lesson)
    images = Image.objects.filter(lesson=lesson)
    documents = Document.objects.filter(lesson=lesson)
    urls = Url.objects.filter(lesson=lesson)


    form = LessonForm(instance=lesson)
    form1 = UrlForm


    if request.method == 'POST' and 'LessonForm' in request.POST: #for editing the lesson
        form = LessonForm(request.POST,instance=lesson)
        if form.is_valid:
            form.save()
            messages.success(request, "la leçon a été modifiée.")
            return redirect('edit_lesson',lesson.id)

    if request.method == 'POST' and 'UrlForm' in request.POST:  #for creating a new url
        form = UrlForm(request.POST)
        if form.is_valid:
            instance = form.save(commit=False)
            instance.lesson = lesson
            instance.save()
            messages.success(request, "Url a été enregistrées.")#sucssess messages: edit the massege that shows between the brackets
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
    return render(request,'lesson/edit_lesson.html',context)


def delete_lesson(request,pk):
    lesson = Lesson.objects.get(pk=pk)
    lesson.delete()
    messages.warning(request, "une Leçon a été supprimée avec succès!")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

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
    return render(request,'lesson/add_lesson_video.html',context)

def edit_lesson_video(request,lesson_id,pk):
    lesson = Lesson.objects.get(id=lesson_id)
    video = Video.objects.get(pk=pk)
    form = VideoForm(instance=video)
    if request.method == 'POST':
        form = VideoForm(request.POST,request.FILES,instance=video)
        if form.is_valid():
            form.save()
            messages.success(request, "la vidéo a été modifiée.")
            return redirect('edit_lesson',lesson_id)
    context = {
        'form':form,
        'lesson':lesson,
    }
    return render(request,'lesson/add_lesson_video.html',context)

def delete_lesson_video(request,pk):
    video = Video.objects.get(pk=pk)
    video.delete()
    messages.warning(request, "une vidéo a été supprimée avec succès!")
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
            messages.warning(request, "aucune image ajoutée")
        return redirect('edit_lesson',lesson_id)

    return render (request,'lesson/add_lesson_image.html')


def edit_lesson_image(request,lesson_id,pk):
    lesson = Lesson.objects.get(id=lesson_id)
    image = Image.objects.get(pk=pk)
    form = ImageForm(instance=image)
    if request.method == 'POST':
        form = ImageForm(request.POST,request.FILES,instance=image)
        if form.is_valid():
            form.save()
            messages.success(request, "l'image a été modifiée.")
            return redirect('edit_lesson',lesson_id)
    context = {
    'form':form,
    'lesson':lesson,
    'image':image,
   }
    return render(request,'lesson/edit_lesson_image.html',context)


def delete_lesson_image(request,pk):
    image = Image.objects.get(pk=pk)
    image.delete()
    messages.warning(request, "un image a été supprimée avec succès!")
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
    return render(request,'lesson/add_lesson_document.html',context)

def edit_lesson_document(request,lesson_id,pk):
    lesson = Lesson.objects.get(id=lesson_id)
    document = Document.objects.get(pk=pk)
    form = DocumentForm(instance=document)
    if request.method == 'POST':
        form = DocumentForm(request.POST,request.FILES,instance=document)
        if form.is_valid():
            form.save()
            messages.success(request, "Le document a été modifiée.")
            return redirect('edit_lesson',lesson_id)
    context = {
    'form':form,
    'lesson':lesson,
   }
    return render(request,'lesson/add_lesson_document.html',context)


def delete_lesson_document(request,pk):
    document = Document.objects.get(pk=pk)
    document.delete()
    messages.warning(request, "une document a été supprimée avec succès!")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))



#==========================lesson Url delete=========================
def delete_lesson_url(request,pk):
    url = Url.objects.get(pk=pk)
    url.delete()
    messages.warning(request, "une Url a été supprimée avec succès!")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))




#========================== global form stuff=====================================
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from client.models import School

class GlobalLessonView(CreateView):
    model = Lesson
    form_class = GlobalLessonForm
    success_url = reverse_lazy('globalform')
    
    def get_form_kwargs(self):#this is for passing (request) to form
        kwargs = super().get_form_kwargs()
        kwargs.update(request=self.request)
        return kwargs

def load_subjects(request):
    level_id = request.GET.get('level')
    subjects = Subject.objects.extra(where=[db_name+'.scolarité_subject.id in( select subject_id from '+db_name+'.scolarité_levelsubject where level_id='+level_id+')'])
    return render(request, 'lesson/subject_dropdown_list_options.html', {'subjects': subjects})

