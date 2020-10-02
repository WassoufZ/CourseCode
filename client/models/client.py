from django.db import models
from django.conf import settings

class Client(models.Model):
    name = models.CharField(max_length=100,verbose_name="Nom", blank=False)
    name_arabic = models.CharField(max_length=100,verbose_name="Nom en arabe", blank=False)
    tel_number1 = models.CharField(max_length=100,verbose_name="Téléphone 1",null=True, blank=False)
    tel_number2 = models.CharField(max_length=100,verbose_name="Téléphone 2",null=True,blank=True)
    email1 = models.EmailField(verbose_name="e-mail 1",null=True, blank=False)
    email2 = models.EmailField(verbose_name="e-mail 2",null=True,blank=True)
    adresse = models.CharField(max_length=200,verbose_name="Adresse", null=True,blank=False)

    #image = models.FileField(null=True, blank=True)
    image = models.ImageField(upload_to="photos/")

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True,related_name='created_by')
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False,
                                verbose_name="Date de parution")
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True,related_name='updated_by')
    updated_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name