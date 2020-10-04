from django.conf.urls import url
from . import views


urlpatterns = [
    
    url(r'^view_lessons/$', views.view_lessons, name="view_lessons"),  
    url(r'^add_lesson/$', views.add_lesson, name="add_lesson"),
    url(r'^delete_lesson/(\d+)/$', views.delete_lesson, name="delete_lesson"),  
    url(r'^lesson_info/(\d+)/$', views.lesson_info, name="lesson_info"), 
    
    url(r'^lesson_info/(\d+)/add_lesson_video/$', views.add_lesson_video, name="add_lesson_video"),
    url(r'^lesson_info/(\d+)/edit_lesson_video/(\d+)/$', views.edit_lesson_video, name="edit_lesson_video"),  
    url(r'^delete_lesson_video/(\d+)/$', views.delete_lesson_video, name="delete_lesson_video"),  
  
    url(r'^lesson_info/(\d+)/add_lesson_image/$', views.add_lesson_image, name="add_lesson_image"),

    url(r'^lesson_info/(\d+)/upload_images/$', views.upload_images, name="upload_images"),


    url(r'^lesson_info/(\d+)/edit_lesson_image/(\d+)/$', views.edit_lesson_image, name="edit_lesson_image"),  
    url(r'^delete_lesson_image/(\d+)/$', views.delete_lesson_image, name="delete_lesson_image"),

  

 
]
