from django import forms

#import models
from .models import Candidate, Job


class ApplyForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ['name', 'email', 'website', 'resume', 'cover_letter']


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ('slug',)

