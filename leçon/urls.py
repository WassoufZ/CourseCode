from django.conf.urls import url
from . import views


urlpatterns = [
    
    url(r'^view_lessons/$', views.view_lessons, name="view_lessons"),  
    url(r'^add_lesson/$', views.add_lesson, name="add_lesson"),  
 
]
