from django import forms
from .models import TrainingReview

class ReviewForm(forms.ModelForm):

    class Meta:
        model = TrainingReview
        fields = ['context', 'rating']
        