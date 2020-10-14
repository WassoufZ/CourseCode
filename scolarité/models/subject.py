from django.db import models
from django.db.models import CharField, Model
#from django_mysql.models import ListCharField

from client.models import School,Schoolyear

from .level import Level


class Subject(models.Model):

    name = models.CharField(max_length=100,verbose_name="Nom de la matière")
    name_arabic = models.CharField(max_length=100,verbose_name="Nom de la matière (Arabe)", blank=False)
    code = models.CharField(max_length=100,verbose_name="Code ")
    date = models.DateTimeField(auto_now_add=True, auto_now=False,
                                verbose_name="Date de parution")
    updated = models.DateTimeField(auto_now=True)
    school = models.ForeignKey(School, related_name='subjects',on_delete=models.CASCADE)

    schoolyear = models.ForeignKey(Schoolyear,null=True,on_delete=models.CASCADE)
    #level = models.ForeignKey(Level,on_delete=models.CASCADE)# this is adedd  to work with the globalform using subject 
    def __str__(self):
      
        return self.name
    class Meta:
        ordering=["-date"]