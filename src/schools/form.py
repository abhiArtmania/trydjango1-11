from django import forms

class SchoolCreateForm(forms.Form):
    name = forms.CharField()
    location = forms.CharField(required=False)

    def clean_name(self):   # Validation for name field
        name = self.cleaned_data.get("name")
        if name == 'Name':
            raise forms.ValidationError("Not a valid name")
        return name
