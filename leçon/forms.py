from django import forms
from .models import Lesson,Url


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(LessonForm, self).__init__(*args, **kwargs)
        self.fields['level_id'].widget.attrs={'class':'form-control','placeholder': 'Level id'}
        self.fields['subject_id'].widget.attrs={'class':'form-control','placeholder': 'Subject id'}
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
        model = Url
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super(VideoForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs={'class':'form-control','placeholder': 'title'}
        self.fields['video'].widget.attrs={'class':'form-control','placeholder': 'video'}
