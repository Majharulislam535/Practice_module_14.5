from django import forms
import datetime
from django.forms.widgets import NumberInput


class FormApi(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(
        label = 'Please enter your email address'
    )
    date = forms.DateField(initial=datetime.date.today, widget=NumberInput(attrs={'type':'date'}))
    value = forms.DecimalField()

    FV_COLOR = [ ('blue','Blue'),('green','Green'),('black','Black')]
    Favorite_color = forms.ChoiceField(choices=FV_COLOR)
    Favorite_color2 = forms.ChoiceField(choices=FV_COLOR,widget=forms.RadioSelect)

    FV_FRUITS = [ ('apple','Apple'),('orange','Orange'),('Watermelon','Watermelon')]
    Favorite_Fruits = forms.MultipleChoiceField(choices=FV_FRUITS)
    Favorite_Fruits2 = forms.MultipleChoiceField(choices=FV_FRUITS,widget=forms.CheckboxSelectMultiple)


    comment1 = forms.CharField(widget=forms.Textarea)
    comment2 = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    Agree = forms.BooleanField()