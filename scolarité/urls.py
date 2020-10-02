
from django.conf.urls import url
from . import views


urlpatterns = [


    # ------- Admin List Account URL -------


    url(r'^home$', views.levelsList, name="scolarité_home"),  


    # ------- Levels  URL -------

    url(r'^level/list$', views.levelsList, name='levels_list'),

    
    url(r'^subjects/list$', views.subjectsList, name='subjects_list'),
    

    url(r'^level/(?P<level_id>\d+)/subject/list$', views.readLevelSubjectList, name='read_level_subject_list'),
   
]
