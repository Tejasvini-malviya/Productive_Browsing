# forms.py
from django import forms
from .models import *

class RestrictedSiteForm(forms.ModelForm):
    class Meta:
        model = RestrictedSite
        fields = ['url']

class TimeLimitForm(forms.ModelForm):
    class Meta:
        model = TimeLimit
        fields = ['url', 'time_limit']
