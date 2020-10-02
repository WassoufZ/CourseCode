from django import forms
from django.forms import ModelForm
from users.models import User
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from client.validators import validate_email


class RegistrationForm(ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': "form-control", 'placeholder': "Email"}),label=_('Email'), max_length=100,required=True,validators=[validate_email])

    
    class Meta:
        model = User
        fields = ('email',)