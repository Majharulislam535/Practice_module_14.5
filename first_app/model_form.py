from django import forms
from django.forms.widgets import NumberInput
import datetime
from .import models



class ShowModelFrom(forms.ModelForm):
       class Meta:
           model = models.ModelForms
           fields = '__all__'
           labels={
             'name':'Std_Name',
             'date':'Birthday'
           }
           widgets  = {
            'date' : NumberInput(attrs={'type': 'date'}),
        }