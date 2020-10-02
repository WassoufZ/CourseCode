from django.http import HttpResponse
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model as User1
from django.contrib.auth import authenticate, login
from django import forms
from django.contrib.auth.decorators import login_required
from scolarité.models import Admin 
from .forms import LoginForm
from client.models import Agent
from django.http import JsonResponse
from json import dumps
from django.core import serializers
from django.contrib.auth import logout
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _

def logoutUser(request):
    
    logout(request)

    return redirect('login')

def index(request):

    user = request.user
    
    if user.user_type == 'agent':
        return  redirect('agents_list')

    elif user.user_type == 'school_admin':
        return  redirect('scolarité_home')

def test(request):
    if request.user.is_authenticated :
        return HttpResponse("user authenticated "+ request.user.email)
    else: return  HttpResponse('user not authenticated')

def loginUser(request):

    error = False
    form = LoginForm(request.POST)
    if request.method == 'POST':
        
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            email=email.lower()
        #email = request.POST.get("email")
        #pwd = request.POST.get("password")
        #nothing = request.POST.get('not')
            #agents = len(Agent.objects.all())
            user = authenticate(email=email, password=password)
            

            if user is not None:
                if user.last_login == None : 
                    test_login=False
                else:
                    test_login=True
                login(request, user)
                if user.is_confirmed == False : 
                    logout(request)
                    messages.warning(request, _('Veuillez activez votre compte en cliquant sur le lien envoyé sur votre boite email '))

                    return  redirect('login')
                    
                elif user.user_type == 'agent':
                    agent = Agent.objects.filter(account__id=user.id).first()
                    if agent is not None:
                        request.session['agent_id']= agent.id
                        return redirect('client_home')
                        #return HttpResponse('user authenticated '+str(request.session['agent_id'])+' '+user.user_type)
                    else: 
                        #return HttpResponse("account not found")
                        messages.error(request, _('Email ou mot de passe invalide. '))
                        return  redirect('login')
                    
                elif user.user_type == 'school_admin':
                    admin = Admin.objects.filter(account__id=user.id).first()
                    if admin is not None:
                        request.session['admin_id']= admin.id
                        request.session['school_id'] = admin.school.id
                        return redirect('scolarité_home')
                        #return HttpResponse('user authenticated '+str(request.session['school_id'])+' '+user.user_type)
                    else: 
                        messages.error(request, _('Email ou mot de passe invalide. '))
               
                        return  redirect('login')

                else: return HttpResponse('user authenticated : '+email)
            else:  

                messages.error(request, _('Email ou mot de passe invalide '))
               
                return  redirect('login')

                #return HttpResponse('the user was not found mot de passe ou email erronée '+str(user) )
                #error = True
            #return HttpResponse('the user was not found ' )

                
        else:
                #return HttpResponse('user not found')
                # sinon une erreur sera affichée
       
            error = True

    #else:    return render(request, 'login.html')
    else:
        form = LoginForm()

    return render(request, 'login.html', locals())

def custom_404(request):
    return render(request,'error_404.html')

def custom_500(request):
    return render(request,'error_404.html')

# Create your views here.
