from django import forms
from .models import *


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = '__all__'
        exclude = ['subject','level','views']

    def __init__(self, *args, **kwargs):
        super(LessonForm, self).__init__(*args, **kwargs)
        self.fields['chapiter'].widget.attrs={'class':'form-control','placeholder': 'Chapiter'}
        self.fields['lesson'].widget.attrs={'class':'form-control','placeholder': 'Lesson'}
        self.fields['skill'].widget.attrs={'class':'form-control','placeholder': 'Skill'}
        self.fields['vacations'].widget.attrs={'class':'form-control','placeholder': 'Vacations'}
        self.fields['link'].widget.attrs={'class':'form-control','placeholder': 'Link'}
        self.fields['order'].widget.attrs={'class':'form-control','placeholder': 'Order'}
        self.fields['remarques'].widget.attrs={'class':'form-control','placeholder': 'Remarques'}
        self.fields['state'].widget.attrs={'class':'switchery'}

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = '__all__'
        exclude = ['lesson']
    def __init__(self, *args, **kwargs):
        super(VideoForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs={'class':'form-control','placeholder': 'title'}
        #self.fields['video'].widget.attrs={'class':'file-styled'}

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
        exclude = ['lesson']
    def __init__(self, *args, **kwargs):
        super(ImageForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs={'class':'form-control','placeholder': 'title'}
        #self.fields['image'].widget.attrs={'class':'file-styled'}

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = '__all__'
        exclude = ['lesson']
    def __init__(self, *args, **kwargs):
        super(DocumentForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs={'class':'form-control','placeholder': 'title'}
        #self.fields['image'].widget.attrs={'class':'file-styled'}

class   UrlForm(forms.ModelForm):
    class Meta:
        model = Url
        fields = '__all__'
        exclude = ['lesson']
    def __init__(self, *args, **kwargs):
        super(UrlForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs={'class':'form-control','placeholder': 'title'}
        self.fields['link'].widget.attrs={'class':'form-control','placeholder': 'Url'} 

#=========================global form stuff=====================================

from django.conf import settings
db_name = settings.DATABASES['default']['NAME']

class GlobalLessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = '__all__'
        #exclude = ['views'] #if you want to control the views count remove the '#'

    def __init__(self, request, *args, **kwargs):
        school_id = request.session['school_id']
        super().__init__(*args, **kwargs)
        #self.fields['subject'].queryset = Subject.objects.none() #change to .all() to see list of all subjects
        self.fields['level'].queryset = Level.objects.filter(school__id= school_id)

       
