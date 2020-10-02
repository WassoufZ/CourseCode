from django import forms

class EmailForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': "form-control", 'placeholder': "E-mail"}),max_length=100,required=True)
    
    
    