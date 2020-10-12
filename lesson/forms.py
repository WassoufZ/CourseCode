from django import forms
from .models import *


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = '__all__'
        exclude = ['subject','level']

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


class GlobalLessonForm(forms.ModelForm):
    class Meta:
        model = GlobalLesson
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subject'].queryset = LevelSubject.objects.none()

        if 'level' in self.data:
            try:
                level_id = int(self.data.get('level'))
                self.fields['subject'].queryset = LevelSubject.objects.filter(level_id=level_id)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['subject'].queryset = self.instance.level.levelsubject_set