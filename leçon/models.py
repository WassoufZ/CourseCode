from django.db import models

class Lesson(models.Model):
    level_id = models.CharField(max_length=200)
    subject_id = models.CharField(max_length=200)
    chapiter = models.CharField(max_length=200)
    lesson = models.CharField(max_length=200)
    skill = models.CharField(max_length=200)
    vacations = models.IntegerField()
    link = models.CharField(max_length=700)
    remarques = models.TextField()
    order = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now=True)
    state = models.BooleanField(default=False)

    def __str__(self):
        return self.level_id

class Video(models.Model):
    lesson = models.ForeignKey(Lesson,on_delete=models.CASCADE,blank=True,null=True)
    title = models.CharField(max_length=200)
    video = models.FileField()
    def __str__(self):
        return self.title


class Image(models.Model):
    lesson = models.ForeignKey(Lesson,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    image = models.ImageField()
    def __str__(self):
        return self.title


class Document(models.Model):
    lesson = models.ForeignKey(Lesson,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    document = models.FileField()
    def __str__(self):
        return self.title


class Url(models.Model):
    lesson = models.ForeignKey(Lesson,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    def __str__(self):
        return self.title

