from django.db import models
from django.db.models import CharField, Model
from client.models import School,Schoolyear
from . import Subject,Level



class LevelSubject(models.Model):
    coefficient = models.IntegerField(default=1)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    level = models.ForeignKey(Level,on_delete=models.CASCADE)

    schoolyear = models.ForeignKey(Schoolyear,null=True,on_delete=models.CASCADE)

    date = models.DateTimeField(auto_now_add=True, auto_now=False,verbose_name="Date de parution")
    updated = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que
        nous traiterons plus tard et dans l'administration
        """
        return self.subject#.name  #add this to return the name of the subject 