from django import forms
from .models import *
from django.forms.widgets import *

class PatternAddForm(forms.ModelForm):
    class Meta:
        model = Pattern
        fields = ('Name','Blueprint','Photo','Gcode','Duration','Description','Type')
