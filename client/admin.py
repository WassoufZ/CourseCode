from django.contrib import admin
from .models import Client

"""class ClientAdmin(admin.ModelAdmin):
    list_display   = ('name', 'nb_eleves','nb_parents', 'paiement','actif')
    list_filter    = ('name','actif','nb_eleves')
    date_hierarchy = 'date'
    ordering       = ('date', )
    search_fields  = ('name',)
    #fields = ( 'auteur', 'titre','categorie', 'contenu')
    fieldsets = (
    # Fieldset 1 : meta-info (titre, auteur…)
   ('Général', {
        'classes': ['collapse',],
        'fields': ('name', 'tel_numbers', 'emails', 'actif')
    }),
    # Fieldset 2 : contenu de l'article
    ('Abonnement', {
       'description': 'information liées aux paiements !',
       'fields': ('nb_eleves','nb_parents','nb_enseignants','nb_administrateurs','paiement', )
    }),
)

admin.site.register(Client,ClientAdmin)"""


# Register your models here.
