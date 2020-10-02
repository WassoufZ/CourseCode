from django.conf.urls import url
from . import views


urlpatterns = [
    
    url(r'^view_lessons/$', views.view_lessons, name="view_lessons"),  
    url(r'^add_lesson/$', views.add_lesson, name="add_lesson"),
    url(r'^delete_lesson/(\d+)/$', views.delete_lesson, name="delete_lesson"),  
    url(r'^lesson_info/(\d+)/$', views.lesson_info, name="lesson_info"), 
    url(r'^lesson_info/(\d+)/add_lesson_video/$', views.add_lesson_video, name="add_lesson_video"),  
 

 
]
