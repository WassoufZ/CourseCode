from django.db import models
from .client import Client
from .schoolyear import Schoolyear

from datetime import date

from django.conf import settings


#school_types = (('0','Primaire'),('1','CEM'),('3ap','Lycée'),)

school_types = (('primary','Primaire'),('middle','CEM'),('high','Lycée'),)

class School(models.Model):
    name = models.CharField(max_length=100,verbose_name="Nom", blank=False)
    name_arabic = models.CharField(max_length=255,verbose_name="Nom en arabe", blank=False)
    tel_number1 = models.CharField(max_length=100,verbose_name="Téléphone 1",null=True, blank=False)
    tel_number2 = models.CharField(max_length=100,verbose_name="Téléphone 2",null=True)
    email1 = models.EmailField(verbose_name="e-mail 1",null=True, blank=False)
    email2 = models.EmailField(verbose_name="e-mail 2",null=True,blank=True)
    creation_date = models.DateTimeField(auto_now_add=True, auto_now=False ,verbose_name="Date de parution")
    updated = models.DateTimeField(auto_now=True)
    adresse = models.CharField(max_length=200,verbose_name="Adresse", null=True,blank=False)
    approval_number = models.CharField(max_length=100,verbose_name="Numéro de l'agrément", blank=False)
    type = models.CharField(max_length=100,choices=school_types,verbose_name="Type de l'école")
    pupils_number = models.IntegerField(null=True,blank=True)
    client = models.ForeignKey(Client)

    current_schoolyear = models.ForeignKey(Schoolyear, null=True,on_delete=models.SET_NULL,related_name='schoolyears_list')



    def __str__(self):
        return self.name