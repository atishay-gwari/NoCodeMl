
from django import forms
from data.models import *
from django.forms import widgets


class FileForm(forms.ModelForm):
    class Meta:
        model=Dataset
        fields=['file',"public"]