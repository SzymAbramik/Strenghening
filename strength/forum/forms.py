from django import forms
from .models import Post, Comment

class AddPost(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('name', 'context')


class AddComment(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('context',)