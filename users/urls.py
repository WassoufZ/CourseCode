from django.conf.urls import url
from . import views

urlpatterns = [



	# ------- SchoolSuperAdministrator Account URL -------
	url(r'^school/(?P<school_id>\d+)/super-admin/create$', views.addSchoolSuperAdministratorAccount, name='add_school_super_admin_account'),

	# ------- SchoolAdministrator Account URL -------
	#url(r'^school/(?P<school_id>\d+)/admin/create$', views.addSchoolAdministratorAccount, name='add_school_admin_account'),	

	# ------- Parent Account URL -------
	#url(r'^parent/(?P<parent_id>\d+)/create$', views.addParentAccount, name='add_parent_account'),

	# ------- Teacher Account URL -------
	#url(r'^teacher/(?P<teacher_id>\d+)/create$', views.addTeacherAccount, name='add_teacher_account'),

	# ------- User Update Account  URL -------
	#url(r'^(?P<user_id>\d+)/update$', views.updateAccount, name='update_account'),	


	# ------- School User Update Account  URL -------
	#url(r'^school/(?P<user_id>\d+)/update$', views.updateSchoolAccount, name='update_school_account'),	

	# ------- School User Delete Account  URL -------
	#url(r'^school/(?P<user_id>\d+)/delete$', views.deleteSchoolAccount, name='delete_school_account'),

	#url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate'),


	# ------- read profile -------

	#url(r'^user/profile$', views.readUser, name='read_user'),	
	
	#------------------ change password ---------------

	#url(r'^pwd/change$', views.passwordChange, name='password_change'),


	#------------------ password forgot ----------------------

	#url(r'^pwd/forgot$', views.passwordForgot, name='password_forgot'),

	#------------------ password reset by Admin ----------------------

	#url(r'^pwd/reset/(?P<user_id>\d+)/update$', views.passwordSet, name='password_set_user'),



	#------------------ password forgot link ----------------------

	
	#url(r'^pwd/forgot/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.passwordForgotLink, name='password_forgot_link'),

	# ------- School User Update Account  URL -------
	#url(r'^school/profil/update$', views.updateUserProfil, name='update_user_profil'),	

	#url(r'^school/profil/account/update$', views.updateUserProfilAccount, name='update_user_profil_account'),	
]


