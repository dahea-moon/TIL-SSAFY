from django import forms
from .models import Posting


class PostingModelForm(forms.ModelForm):
    class Meta:
        models = Posting
        fields = ('content',)


# class CommentModelForm(forms.ModelForm):
#     class Meta:
#         models = Comment
#         fields = ('content',)