from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .models import User
from client.models import Agent, School
from scolarité.models import Admin
#from scolarité.views import generateEmail,generateUsername,generatePassword
from django.shortcuts import redirect
from scolarité.forms import AdminForm
from FYK.views import logoutUser
from .forms import UserRegistrationForm,RegistrationForm,EmailForm
from django.contrib.auth.models import Permission
from django.contrib.auth.models import Group
from django.core.mail import send_mail
from django.db.models import Q
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .models import tokens 
from django.contrib.auth import logout
import datetime
from datetime import datetime, timedelta



db_name = settings.DATABASES['default']['NAME']

def redirectHome(request):

	user = request.user	
	if user.user_type == 'agent':
		return  redirect('agents_list')

	elif user.user_type == 'school_admin':
		return  redirect('scolarité_home')


def redirectHomePermissionDenied(request):
	
	messages.error(request, _('Accès refusé.'))
	return redirectHome(request)
	
def redirectLogin(request):
	messages.warning(request, _('Vous devez connecter.'))
	return redirect('login')
	
#----------- START AgentAccount Views -----------

#----------- END AgentAccount Views -----------

#generate usernmaes and passwords

def generateEmail(request,username):

    #convert the first and the last name to lowercase
    email_generate=username+'@taalimup.com'

    return email_generate

def generateUsername(request,last_name,first_name,date):

    #convert the first and the last name to lowercase
    last_name_lower=last_name.lower()
    first_name_lower=first_name.lower()
    format_date=date.strftime('%d%M')
    #generate the password - dont make random because the most of them dont have an access with their emails 
    username_generate=first_name_lower[0]+last_name_lower+format_date

    return username_generate

def generatePassword(request,last_name,first_name,date):

    #convert the first and the last name to lowercase
    last_name_lower=last_name.lower()
    first_name_lower=first_name.lower()
    #generate the password - dont make random because the most of them dont have an access with their emails 
    format_date_pwd=date.strftime('%m%y')
    plain_pwd=last_name_lower+format_date_pwd

    return plain_pwd

#----------- START SchoolSuperAdministrator Views -----------

def addSchoolSuperAdministratorAccount(request,school_id):
	
	if not request.user.is_authenticated:
		return redirectLogin(request)
	if not request.user.user_type == 'agent' :
		return redirectHomePermissionDenied(request)  
	try:
		school = School.objects.get(id=school_id)
		if not hasSuperAdmin(school_id) :	
	        # if this is a POST request we need to process the form data
			if request.method == 'POST':
				user_form = User()
				admin = Admin()
				registration_form = RegistrationForm(request.POST or None, instance = user_form)
				admin_form = AdminForm(request.POST or None, instance = admin)
	            # create a form instance and populate it with data from the request:			
				if all([registration_form.is_valid(),admin_form.is_valid()]):
					plain_pwd = User.objects.make_random_password()
					created_user = User.objects.create_user(user_form.email,plain_pwd)
					#created_user = User.objects.create_user(user.email,admin.last_name)
					created_user.user_type = 'school_admin'
					created_user.last_name = admin.last_name
					created_user.first_name = admin.first_name
					created_user.school=school
					created_user.schoolyear = school.current_schoolyear

					created_user.save()

					admin.school = school
					admin.is_super_admin = True
					admin.account = created_user
					admin.schoolyear = school.current_schoolyear
					admin_form.save()
					group = Group.objects.get(name='school administrators')
					created_user.groups.add(group)

					last_name=admin.last_name
					first_name = admin.first_name 
					admin_date = admin.date  

					#generate the email
					username_generate=generateUsername(request,last_name,first_name,admin_date)

					created_user.username=username_generate
					created_user.save()

					#send user name and passwoed to user's email
					to_email = created_user.email
					to_username = created_user.username
					emailInfo(request,to_email,to_username,plain_pwd)
					current_site = get_current_site(request)

					credentials_message = render_to_string('users/credentials_email.html', {
						'pwd':plain_pwd, 
						
					})
					#send activation email to the user
					current_site = get_current_site(request)
					message = render_to_string('users/activate_email.html', {
						'user':created_user, 
						'domain':current_site.domain,
						'uid': urlsafe_base64_encode(force_bytes(created_user.pk)),
		                'token': tokens.account_activation_token.make_token(created_user),
					})
					mail_subject = 'Activate your TaalimUp account.'
					to_email = created_user.email
					send_mail(mail_subject, message, settings.EMAIL_HOST_USER,[to_email],fail_silently=True,)
		            
					envoi = True
					messages.success(request, 'Le compte du super administrator " %s " de l\'école est créé avec succès'%(admin.account.email))
	                # redirect to a new URL:
					return  redirect('update_school', school_id=school.id)
				else:
					messages.error(request, 'Le compte du super administrator n\'est pas créé.')
			else:
				registration_form = RegistrationForm()
				admin_form = AdminForm()
		else: 
			messages.error(request, 'This school already has super admin account.')
    # if the object doesn't exist 
	except School.DoesNotExist:
		messages.warning(request, 'L\'école n\'existe pas')
		return  redirect('update_school', school_id=school.id)

	return  render(request, 'users/add_school_super_admin_account.html',locals())  
	
#----------- END SchoolSuperAdministrator Views -----------


#----------- START hasSuperAdmin Views -----------
	
def hasSuperAdmin(school_id):
	admins = Admin.objects.filter(Q(is_super_admin=True) & Q(school=school_id))
	if (len(admins) > 1): return True
	else: return False

#------------------ read User profil -----------------

