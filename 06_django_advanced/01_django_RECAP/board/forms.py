from django import forms
from .models import Article, Comment

# forms.Form => data 입력 및 검증
# forms.ModelForm => data 입력/검증 + HTML 생성

class ArticleForm(forms.Form):
    title = forms.CharField(min_length=2, max_length=100)
    content = forms.CharField()


class ArticleModelForm(forms.ModelForm):
    # 1. DATA 입력 및 검증
    # 2. HTML 생성

    title = forms.CharField(min_length=2, max_length=100)
    content = forms.Textarea
    class Meta:
        model = Article
        fields = '__all__'      # 모든 항목을 전부 검증

class CommentModelForm(forms.ModelForm):
    content = forms.CharField(min_length=2, max_length=200) # 200이 넘으면 아예 오류남

    class Meta:
        model = Comment
        fields = ('content',)   # content만 검증 // tuple, list 모두 가능한 syntax
