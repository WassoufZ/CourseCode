from django import forms
from django.forms import ModelForm, Textarea
from .models import Client,  Agent
from django.core.exceptions import ValidationError
from .validators import validate_email,validate_arabic
import re
from django.utils.translation import ugettext_lazy as _



school_types = (('primary','Primaire'),('middle','CEM'),('high','Lycée'),)
genders = (('man','Homme'), ('woman','Femme'),) 


