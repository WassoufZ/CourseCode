from django import forms
from .models import Lesson


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = '__all__'

   # def __init__(self, *args, **kwargs):
   #     super(LessonForm, self).__init__(*args, **kwargs)
   #     self.fields['skill'].widget.attrs['class'] = 'form-control'
