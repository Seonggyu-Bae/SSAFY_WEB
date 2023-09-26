from django import forms
from .models import Article

# Form 실습
# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=20)
#     content = forms.CharField(widget=forms.Textarea)

# ModelForm 실습
class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label = '제목',
        widget=forms.TextInput(
            attrs={
                'class' : 'my-title',
                'placeholder' : 'Enter the title',
            }
        ),
    )
    content = forms.CharField(
        label = '내용',
        widget=forms.Textarea(
            attrs={
                'class' : 'my-content',
                'placeholder' : 'Enter the content',
                'rows' : 5,
                'cols' : 50,
            }
        ),
        error_messages={'required' : '내용을 입력해 주세요.'},
    )
    class Meta:
        model = Article
        fields = '__all__'