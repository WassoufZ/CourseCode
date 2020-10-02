from django.db import models
from users.models import Address
from django.conf import settings

genders = (('man','Homme'), ('woman','Femme'),) 
class Agent(models.Model):
    first_name = models.CharField(max_length=100,verbose_name="Prénom", blank=False)
    first_name2 = models.CharField(max_length=100,verbose_name="Prénom 2", blank=False)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(auto_now_add=False, auto_now=False,verbose_name="Date de naissance", null=True)
    place_of_birth = models.CharField(max_length=100,verbose_name="Adresse", null=True)
    tel_number = models.CharField(max_length=100,verbose_name="Tel",null=True)
    tel_number2 = models.CharField(max_length=100,verbose_name="Tel 2", null=True)
    gender = models.CharField(max_length=100,choices=genders,verbose_name="sexe")
    address = models.OneToOneField(Address,null=True)
    date = models.DateTimeField(auto_now_add=True, auto_now=False,
                                verbose_name="Date de parution")
    updated = models.DateTimeField(auto_now=True)

    image = models.ImageField(null=True, blank=True, upload_to="photos/")
    account = models.OneToOneField( settings.AUTH_USER_MODEL,null=True,on_delete=models.SET_NULL)
    def __str__(self):
        return self.first_name +' '+self.last_name