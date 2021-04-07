from django import forms

#import models
from .models import Candidate


class ApplyForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ['name', 'email', 'website', 'resume', 'cover_letter']

