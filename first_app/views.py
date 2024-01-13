from django.shortcuts import render
from .import forms
from .import model_form
from .import models

# Create your views here.

def home(request):
    return render(request,'home.html')

def FormApi(request):
    form = forms.FormApi(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request,'FormApi.html',{'form':form})

def ModelForm(request):
    if request.method=='POST':
        form = model_form.ShowModelFrom(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = model_form.ShowModelFrom()
    return render(request,'ModelForm.html',{'form':form})