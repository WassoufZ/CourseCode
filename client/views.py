from django.http import HttpResponse,Http404
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django import forms
from django.contrib.auth.decorators import login_required
from .models import Client, School,Agent,Schoolyear
#from .forms import ClientForm, SchoolForm
from scolarité.models import Level
from users.models import Address
from users.forms import AddressForm,RegistrationForm
from scolarité.forms import AdminForm
from scolarité.models import Admin,Subject,Level,LevelSubject
from django.shortcuts import redirect
from django.db.models import Q
from django.conf import settings
from django.contrib.auth import get_user_model
from users.views import redirectLogin,redirectHome,redirectHomePermissionDenied
from django.conf import settings

User = get_user_model()
db_name = settings.DATABASES['default']['NAME']
#----------- START UserLogin Views -----------

