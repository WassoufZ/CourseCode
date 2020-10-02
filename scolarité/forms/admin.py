from django import forms
from django.forms import ModelForm
from scolarité.models import Admin
from django.utils.translation import ugettext_lazy as _
from client.validators import validate_name

genders = (('man','Homme'), ('woman','Femme'),) 

class AdminForm(ModelForm):

    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': "form-control", 'placeholder': "Prénom 1"}),label=_('Prénom'), max_length=100,required=True,validators=[validate_name])
    first_name2 = forms.CharField(widget=forms.TextInput(
        attrs={'class': "form-control", 'placeholder': "Prénom 2"}),label=_('Prénom'), max_length=100,required=False,validators=[validate_name])
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': "form-control", 'placeholder': "Nom"}),label=_('Nom'), max_length=100,required=True,validators=[validate_name])
    date_of_birth = forms.DateField(widget=forms.TextInput(
        attrs={'class': "form-control", 'placeholder': "2012-02-08",'type': 'date'}),label=_('Date de naissance'), required=True)
    place_of_birth = forms.CharField(widget=forms.TextInput(
        attrs={'class': "form-control", 'placeholder': "Lieu de naissance"}),label=_('Lieu de naissance'), max_length=100,required=False)
    tel_number = forms.CharField(widget=forms.TextInput(
        attrs={'class': "form-control", 'placeholder': "Téléphone 1"}),label=_('Téléphone'), max_length=100,required=True)
    tel_number2 = forms.CharField(widget=forms.TextInput(
        attrs={'class': "form-control", 'placeholder': "Téléphone 2"}),label=_('Téléphone'), max_length=100,required=False)
    gender = forms.ChoiceField(widget=forms. Select(
        attrs={'class': "form-control",'placeholder': "Sexe"}),label=_('Sexe'),choices = genders,required=True)
       
    class Meta:
        model = Admin
        fields = ('first_name', 'first_name2', 'last_name','date_of_birth','place_of_birth',
            'tel_number','tel_number2','gender')
   
