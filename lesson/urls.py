from django.conf.urls import url
from . import views


urlpatterns = [
    
    url(r'^view_lessons_list/(\d+)/$', views.view_lessons_list, name="view_lessons_list"),  
    url(r'^add_lesson/$', views.add_lesson, name="add_lesson"),
    url(r'^delete_lesson/(\d+)/$', views.delete_lesson, name="delete_lesson"),  
    url(r'^edit_lesson/(\d+)/$', views.edit_lesson, name="edit_lesson"),
    url(r'^view_lesson/(\d+)/$', views.view_lesson, name="view_lesson"),

    url(r'^view_lessons_videos/$', views.VideosView.as_view(), name="view_lessons_videos"),
    url(r'^view_lessons_images/$', views.ImagesView.as_view(), name="view_lessons_images"),
    url(r'^view_lessons_documents/$', views.DocumentsView.as_view(), name="view_lessons_documents"),

    url(r'^search/$', views.SearchView.as_view(), name="search"),  

    url(r'^edit_lesson/(\d+)/add_lesson_video/$', views.add_lesson_video, name="add_lesson_video"),
    url(r'^edit_lesson/(\d+)/edit_lesson_video/(\d+)/$', views.edit_lesson_video, name="edit_lesson_video"),  
    url(r'^delete_lesson_video/(\d+)/$', views.delete_lesson_video, name="delete_lesson_video"),  
  
    url(r'^edit_lesson/(\d+)/add_lesson_image/$', views.add_lesson_image, name="add_lesson_image"),
    url(r'^edit_lesson/(\d+)/edit_lesson_image/(\d+)/$', views.edit_lesson_image, name="edit_lesson_image"),  
    url(r'^delete_lesson_image/(\d+)/$', views.delete_lesson_image, name="delete_lesson_image"),

    url(r'^edit_lesson/(\d+)/add_lesson_document/$', views.add_lesson_document, name="add_lesson_document"),
    url(r'^edit_lesson/(\d+)/edit_lesson_document/(\d+)/$', views.edit_lesson_document, name="edit_lesson_document"),  
    url(r'^delete_lesson_document/(\d+)/$', views.delete_lesson_document, name="delete_lesson_document"),

    url(r'^delete_lesson_url/(\d+)/$', views.delete_lesson_url, name="delete_lesson_url"),

    url(r'^globalform/', views.GlobalLessonView.as_view(), name='globalform'),

              #===================== Ajax =====================================

    url(r'^ajax/load-subjects/', views.load_subjects, name='ajax_load_subjects'), 
    url(r'^ajax/ajax_document_views/(\d+)/$', views.ajax_document_views, name='ajax_document_views'),
    url(r'^ajax/ajax_image_views/(\d+)/$', views.ajax_image_views, name='ajax_image_views'),
    url(r'^ajax/ajax_video_views/(\d+)/$', views.ajax_video_views, name='ajax_video_views'),

 
]