from django.db import models

genders = (('0','Femme'),('1','Homme'))

class Address(models.Model):
	country_name = models.CharField(max_length=100,verbose_name="Pays", null=True, blank=True)
	country_code = models.CharField(max_length=100,verbose_name="Code Pays", blank=True, null = True)

	state_name = models.CharField(max_length=100,verbose_name="Wilaya", blank=False)
	state_code = models.CharField(max_length=100,verbose_name="Code Wilaya", blank=True, null = True)

	street_address = models.CharField(max_length=100,verbose_name="Rue", blank=True, null = True)
	postal_code = models.IntegerField(null=True)
	



