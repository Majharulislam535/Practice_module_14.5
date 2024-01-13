from django.db import models

# Create your models here.

class ModelForms(models.Model):
    
    name = models.CharField(max_length=30,default='Rohim')
    roll = models.IntegerField(primary_key=True)
    email = models.EmailField()
    age = models.FloatField(blank=True)
    date = models.DateField(blank=True)
    comment= models.TextField(blank=True)
    Agree = models.BooleanField(blank=True)

    def __str__(self):
        return  f'{self.name}'   