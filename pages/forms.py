from django import forms
from .models import Book , Categrymodel
class Categoryform(forms.ModelForm):
      class Meta:
            model = Categrymodel
            fields=['name']
            widgets ={
                  'name':forms.TextInput(attrs={'class':'form-control'})
            }






class Form(forms.ModelForm):
        class Meta:
            model = Book
            fields = [
                  'title',
                  'outher',
                  'Categry',
                  'status',
                  'active',
                  'outherimage',
                  'image',
                  'retalperiod',
                  'retalprice',
                  'price',
                  'pages',
                      ]
            widgets = {
                   'title':forms.TextInput(attrs={'class':'form-control'}),
                   'outher':forms.TextInput(attrs={'class':'form-control'}),
                   'Categry':forms.Select(attrs={'class':'form-control'}),
                   'status':forms.Select(attrs={'class':'form-control'}),
                   'active':forms.TextInput(attrs={'class':'form-control'}),
                   'outherimage':forms.FileInput(attrs={'class':'form-control'}),
                   'image':forms.FileInput(attrs={'class':'form-control'}),
                   'retalperiod':forms.TextInput(attrs={'class':'form-control'}),
                   'retalprice':forms.TextInput(attrs={'class':'form-control'}),
                   'price':forms.NumberInput(attrs={'class':'form-control'}),
                   'pages':forms.NumberInput(attrs={'class':'form-control'}),
                   
            }

