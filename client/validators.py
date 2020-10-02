from django import forms
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import re
 

"""def validate_email(data):
        #data = self.cleaned_data['email1']
        if "fred@example.com" not in data:
            raise forms.ValidationError("You have forgotten about Fred!")
        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return data"""


def validate_email(data):   
	email_validator = EmailValidator() 
	try:
		email_validator(data)
	except:
		raise forms.ValidationError(_("Introduisez un email valid"))
	return data

def validate_arabic(data):   
	if re.findall(u'[^\u0621-\u06ED\W]', data, flags=re.UNICODE):
		raise forms.ValidationError(_("Le champs doit étre en langue Arabe!"))
	return data

def validate_name(data):   
	if not data.isalpha() :
		raise forms.ValidationError(_('Veuillez entrer des caractères Alphabétiques A à Z seulement sans espace.'))
	return data

"""
def clean_name_arabic(data):
    if re.findall(u'[^\u0621-\u06ED\W]', data, flags=re.UNICODE):
        raise forms.ValidationError(_("You have forgotten about Fred!"))
    return data"""


