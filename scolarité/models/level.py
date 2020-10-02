from django.db import models
from django.db.models import CharField, Model
from client.models import School,Schoolyear
from django.utils.translation import ugettext_lazy as _



branch_type = (('Math','Mathématique'),('Scientifique','Scientifique'),)

level_types = (('primary','Primaire'),('middle','CEM'),('high','Lycée'),)

#level_types = (('0','Primaire'),('1','CEM'),('3ap','Lycée'),)

class Level(models.Model):
    name = models.CharField(max_length=100,verbose_name="Nom du niveau scolaire")
    name_arabic = models.CharField(max_length=100,verbose_name="Nom de la matière (Arabe)", blank = False)
    code = models.CharField(max_length=100,verbose_name="Code ")
    code_arabic = models.CharField(max_length=100,verbose_name="Code arabic")
    

    type =  models.CharField(max_length=100,choices=level_types,verbose_name="Type",null = True,blank=True)
    branch =  models.CharField(max_length=100,choices=branch_type,verbose_name="Branche",null = True,blank=True)

    school = models.ForeignKey(School,null=True,on_delete=models.CASCADE)
    rank = models.IntegerField(default=0)
    
    date = models.DateTimeField(auto_now_add=True, auto_now=False,verbose_name="Date de parution")
    updated = models.DateTimeField(auto_now=True)

    schoolyear = models.ForeignKey(Schoolyear,null=True,on_delete=models.CASCADE)


    #created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    #updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    def __str__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que
        nous traiterons plus tard et dans l'administration
        """
        return self.name