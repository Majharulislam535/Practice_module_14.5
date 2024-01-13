from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('formApi/',views.FormApi,name='formApi'),
    path('ModelForm/',views.ModelForm,name='ModelForm'),
]
