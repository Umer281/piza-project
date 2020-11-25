from django import forms
from .models import Piza
from django.forms import ModelForm
#from django.db import models

class PizaOrderForm(ModelForm):
    class Meta:
        model=Piza
        fields=['piza_shape','piza_size','piza_topping']


