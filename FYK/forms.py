from django import forms
from django.forms import ModelForm, Textarea
import re
from django.utils.translation import ugettext_lazy as _

genders = (('man','Homme'), ('woman','Femme'),) 

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': "form-control", 'placeholder': "Email"}),label=_('Email'), max_length=100,required=True)
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': "form-control", 'placeholder': "mot de passe"}),label=_('Mots de passe'), required=True)
 


class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(
        attrs={'class': "form-control", 'placeholder': "Email / Nom d'utilisateur"}),label=_('Email'), max_length=100,required=True)
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': "form-control", 'placeholder': "Mot de passe"}),label=_('Mots de passe'), required=True)