from django import forms

class SchoolCreateForm(forms.Form):
    name = forms.CharField()
    location = forms.CharField(required=False)
