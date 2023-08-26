from django import forms
from django.core import validators
from .models import BlogPost
from tinymce.widgets import TinyMCE

def min_length_3(value):
    if len(value) < 3:
        raise forms.ValidationError("Kendi Denetimimiz... en az 3 karakter olmali..")

class BlogPostModelForm(forms.ModelForm):
    tag = forms.CharField()
    # content = forms.CharField(widgets = TinyMCE(attrs={'cols': 40, 'rows': 20}))
    # title = forms.CharField(validators=[validators.MinLengthValidator(3, message='Oppss.. en az 3 karakter olmali...')])
    title = forms.CharField(validators=[min_length_3,])
    
    
    class Meta:
        model = BlogPost
        widgets = {'content': TinyMCE(attrs={'cols': 40, 'rows': 20})}
        fields = [
            'title',
            'cover_image',
            'content',
            'category',
            'tag',
        ]

    # def clean_title(self):
    #     title = self.cleaned_data.get('title')
    #     if len(title) < 3:
    #         raise forms.ValidationError('Ooo En az 3 karakter olmali...')
    #     return title
