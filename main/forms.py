from django import forms

from .models import *


class NewsPostForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'desc', 'photo', 'category']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder':  'Комментарии',
                'rows': 10
            })
        }


