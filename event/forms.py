from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder' : '내용을 입력하세요',
                }),
            'contents' : forms.Textarea(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : '내용을 입력하세요',
                }),
        }
        
        labels = {
            'title':'제목',
            'content':'내용',
        }
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
