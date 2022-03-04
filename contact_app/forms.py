from dataclasses import field, fields
from django import forms
from .models import Name,PhoneNumbers,Email,Scode

class NameForm(forms.ModelForm):
    class Meta:
        model = Name
        fields =['name']   

class PhoneNumbersForm(forms.ModelForm):
    class Meta:
        model = PhoneNumbers
        fields = ['mobile']

class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['email']

class ScodeForm(forms.ModelForm):
    class Meta:
        model = Scode
        fields = ['scode']