from django.db import models
from django.db.models import CharField, Model




class Schoolyear(models.Model):
	
    start_date = models.DateField(auto_now_add=False, auto_now=False)
    end_date = models.DateField(auto_now_add=False, auto_now=False)
    label = models.CharField(max_length=50,verbose_name="2018-2017")


    starts_at = models.CharField(max_length=50,verbose_name="commence à")
    ends_at = models.CharField(max_length=50,verbose_name="se termine à")

    name = models.CharField(max_length=100,verbose_name="Année Scolaire",null=True)
    arabic_name = models.CharField(max_length=100,verbose_name="Année Scolaire",null=True)

    date = models.DateTimeField(auto_now_add=True, auto_now=False,
                                verbose_name="Date de parution")
    updated = models.DateTimeField(auto_now=True)


    #school = models.ForeignKey(School,null=True,on_delete=models.CASCADE)

    def __str__(self):
      
        return self.label