from django.db import models
from .validators import *

from scolarité.models.level import Level
from scolarité.models.subject import Subject
from scolarité.models.level_subject import LevelSubject


class Lesson(models.Model):
    level = models.ForeignKey(Level,on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    chapiter = models.CharField(max_length=200)
    lesson = models.CharField(max_length=200)
    skill = models.CharField(max_length=200)
    vacations = models.IntegerField()
    link = models.URLField(max_length=700,null=True,blank=True)
    remarques = models.TextField(null=True,blank=True)
    order = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now=True)
    state = models.BooleanField(default=False)

    def __str__(self):
        return self.lesson

class Video(models.Model):
    lesson = models.ForeignKey(Lesson,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    video = models.FileField(validators=[validate_file_extension])
    def __str__(self):
        return self.title


class Image(models.Model):
    lesson = models.ForeignKey(Lesson, default=None, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.FileField(validators=[validate_image_extension])

    def __str__(self):
        return self.lesson.level_id


class Document(models.Model):
    lesson = models.ForeignKey(Lesson,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    document = models.FileField(validators=[validate_document_extension])
    def __str__(self):
        return self.title


class Url(models.Model):
    lesson = models.ForeignKey(Lesson,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    link = models.URLField(max_length=200)
    def __str__(self):
        return self.title


class GlobalLesson(models.Model):
    level = models.ForeignKey(Level,on_delete=models.CASCADE)
    levelsubject = models.ForeignKey(LevelSubject,on_delete=models.CASCADE)
    chapiter = models.CharField(max_length=200)
    lesson = models.CharField(max_length=200)
    skill = models.CharField(max_length=200)
    vacations = models.IntegerField()
    link = models.URLField(max_length=700,null=True,blank=True)
    remarques = models.TextField(null=True,blank=True)
    order = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now=True)
    state = models.BooleanField(default=False)
    def __str__(self):
        return self.lesson
