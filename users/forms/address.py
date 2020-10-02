from django import forms
from django.forms import ModelForm
from users.models import Address
from django.utils.translation import ugettext_lazy as _

class AddressForm(ModelForm):
    country_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': "form-control", 'placeholder': "Pays"}),label=_('Pays') ,max_length=100,required=False)
    country_code = forms.CharField(widget=forms.TextInput(
        attrs={'class': "form-control", 'placeholder': "Code Pays"}),label=_('Code Pays') ,max_length=100,required=False)

    state_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': "form-control", 'placeholder': "Wilaya"}),label=_('Wilaya') ,max_length=100,required=False)
    state_code = forms.CharField(widget=forms.TextInput(
        attrs={'class': "form-control", 'placeholder': "Code Wilaya"}),label=_('Code Wilaya'), max_length=100,required=False)

    street_address = forms.CharField(widget=forms.TextInput(
        attrs={'class': "form-control", 'placeholder': "Rue"}),label=_('Rue') ,max_length=100,required=False)

    postal_code = forms.IntegerField(widget=forms.TextInput(
        attrs={'class': "form-control", 'placeholder': "Code postal"}),label=_('Code postal'),required=False)

   

    class Meta:
        model = Address
        fields = ('country_name', 'state_name', 'postal_code','street_address')
   