from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Level,Subject, Admin,LevelSubject
from django.shortcuts import redirect
from client.models import School,Schoolyear
from django.views.generic import ListView,DetailView,CreateView
from django.core.urlresolvers import reverse_lazy
from django.core import serializers
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime, timedelta
import datetime
from django.utils.translation import ugettext_lazy as _
from users.views import redirectLogin,redirectHome,redirectHomePermissionDenied
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import Group
import pytz
from django.views.generic import View
from django.template.loader import get_template
import arabic_reshaper
#from bidi.algorithm import get_display
from django.views.generic.edit import FormView
from django.urls import reverse
from django.core.files.storage import FileSystemStorage


db_name = settings.DATABASES['default']['NAME']


def home(request):
    if not request.user.is_authenticated:
        return redirectLogin(request)
    if not request.user.user_type == 'school_admin' :
        return redirectHomePermissionDenied(request) 
    try:
        school_id = request.session['school_id']
        school = School.objects.get(id=school_id)   
        levels_list = Level.objects.filter(school__id= school_id)   
    # if the object doesn't exist 
    except School.DoesNotExist:
        messages.warning(request, 'L\'école n\'existe pas')
        return  redirect('login')
    return render(request, 'scolarité/levels_list_grid.html',locals())


#--------- START Level Views -------------------------------------------

def levelsList(request):
    if not request.user.is_authenticated:
        return redirectLogin(request)
    if not request.user.user_type == 'school_admin' :
        return redirectHomePermissionDenied(request) 
    try:
        school_id = request.session['school_id']
        school = School.objects.get(id=school_id)   
        levels_list = Level.objects.filter(school__id= school_id)   

    # if the object doesn't exist 
    except School.DoesNotExist:
        messages.warning(request, 'L\'école n\'existe pas')
        return  redirect('login')
    return render(request, 'scolarité/levels_list_grid.html',locals())

def levelsListAll(request):
    if not request.user.is_authenticated:
        return redirectLogin(request)
    if not request.user.user_type == 'school_admin' :
        return redirectHomePermissionDenied(request) 
    try:
        school_id = request.session['school_id']
        school = School.objects.get(id=school_id)   
        levels_list = Level.objects.filter(school__id= school_id)   
    except School.DoesNotExist:
        messages.warning(request, 'L\'école n\'existe pas')
        return  redirect('login')
    return render(request, 'scolarité/levels_list_all.html',locals())


def subjectsList(request):
    if not request.user.is_authenticated:
        return redirectLogin(request)
    if not request.user.user_type == 'school_admin' :
        return redirectHomePermissionDenied(request) 
    try:
        school_id = request.session['school_id']
        school = School.objects.get(id=school_id)   
        subjects_list = Subject.objects.filter(school__id= school_id)   
    except School.DoesNotExist:
        messages.warning(request, 'L\'école n\'existe pas')
        return  redirect('login')
    return render(request, 'scolarité/subjects_list.html',locals())

#--------- END Level Views ----------------------------------------------

def readLevelSubjectList(request,level_id):
    if not request.user.is_authenticated:
        return redirectLogin(request)
    if not request.user.user_type == 'school_admin':
        return redirectHomePermissionDenied(request) 
    try:
        level = Level.objects.get(id=level_id) 
        school_id = request.session['school_id']
        school = School.objects.get(id=school_id)    
        if level.school.id == school_id:
            """ la liste des matières pour chaque level"""
            subjects_list = Subject.objects.extra(where=[db_name+'.scolarité_subject.id in( select subject_id from '+db_name+'.scolarité_levelsubject where level_id='+level_id+')'])             
        else:
            return  redirect('scolarité_home')
    # if the object doesn't exist
    except Level.DoesNotExist:
        messages.warning(request, _('Le niveau n\'existe pas.'))
        return  redirect('scolarité_home')
    return render(request, 'scolarité/subjects_list.html',locals())