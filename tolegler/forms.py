from django import forms
from django.contrib.auth.models import User
from .models import*


class TolegForm(forms.ModelForm):
    class Meta:
        model = Toleg
        fields = '__all__'
