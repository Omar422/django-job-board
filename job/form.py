from django import forms
from .models import Apply, Job

class ApplyJob(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ['name', 'email', 'website', 'cv', 'cover_letter']


class AddJob(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__' # all colomuns
        exclude = ('owner', 'slug')