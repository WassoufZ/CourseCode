from django.db import models
#from client.models import School 
#remove it to avoid confilt betwwen two apps
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from .user_manager import UserManager

class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=40, null=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)

    #phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    #phone = models.CharField(_('phone number'), validators=[phone_regex], max_length=17, unique=True) # validators should be a list
    
    user_type = models.CharField(_('type'), max_length=30, blank=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_confirmed = models.BooleanField(_('inscription confirmée'), default=True)

    school = models.ForeignKey('client.School',null=True,on_delete=models.CASCADE)
    #schoolyear = models.ForeignKey('client.schoolyear',null=True,on_delete=models.CASCADE)

    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    objects = UserManager()

    USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.last_name,self.first_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)